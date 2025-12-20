from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Camera-related variables (better viewing angle)
# (x, y, z) -> x sideways, y forward/back, z height
camera_pos = (-450, -650, 520)

fovY = 95
GRID_LENGTH = 600
rand_var = 423


def draw_text(x, y, text, font=GLUT_BITMAP_HELVETICA_18):
    glColor3f(1, 1, 1)
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()

    gluOrtho2D(0, 1000, 0, 800)

    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    glRasterPos2f(x, y)
    for ch in text:
        glutBitmapCharacter(font, ord(ch))

    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)


def keyboardListener(key, x, y):
    pass


def specialKeyListener(key, x, y):
    global camera_pos
    cx, cy, cz = camera_pos

    if key == GLUT_KEY_LEFT:
        cx -= 10
    if key == GLUT_KEY_RIGHT:
        cx += 10
    if key == GLUT_KEY_UP:
        cz += 10
    if key == GLUT_KEY_DOWN:
        cz -= 10

    camera_pos = (cx, cy, cz)


def mouseListener(button, state, x, y):
    pass


def setupCamera():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(fovY, 1.25, 0.1, 2000)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    x, y, z = camera_pos
    gluLookAt(
        x, y, z,      # camera position
        0, 120, 0,    # look-at target (slightly forward so ground looks nicer)
        0, 0, 1       # up vector
    )


def draw_environment():
    """
    Draw:
    - big green plane
    - dark grey road strip in the middle
    - bluish left & right walls
    """

    L = 600  # half length (matches your GRID_LENGTH usage style)

    # Road settings
    road_half_width = 130  # road width = 260
    road_z = 0.5           # tiny lift to avoid z-fighting with ground

    # Wall settings
    wall_height = 380
    wall_thickness = 45

    glBegin(GL_QUADS)

    # ---------- Ground (green) ----------
    glColor3f(0.44, 0.67, 0.29)  # green-ish
    glVertex3f(-L, -L, 0)
    glVertex3f(L, -L, 0)
    glVertex3f(L, L, 0)
    glVertex3f(-L, L, 0)

    # ---------- Road (dark grey strip in middle) ----------
    glColor3f(0.30, 0.30, 0.30)  # dark grey
    glVertex3f(-road_half_width, -L, road_z)
    glVertex3f(road_half_width, -L, road_z)
    glVertex3f(road_half_width, L, road_z)
    glVertex3f(-road_half_width, L, road_z)

    # ---------- Left wall (bluish) ----------
    # A rectangular vertical wall along the left side of the plane.
    glColor3f(0.70, 0.78, 0.92)  # bluish
    left_outer_x = -L
    left_inner_x = -L + wall_thickness

    # Wall face (inner face visible from center)
    glVertex3f(left_inner_x, -L, 0)
    glVertex3f(left_inner_x, L, 0)
    glVertex3f(left_inner_x, L, wall_height)
    glVertex3f(left_inner_x, -L, wall_height)

    # Wall top
    glVertex3f(left_outer_x, -L, wall_height)
    glVertex3f(left_outer_x, L, wall_height)
    glVertex3f(left_inner_x, L, wall_height)
    glVertex3f(left_inner_x, -L, wall_height)

    # Wall outer face (optional but makes it look like a slab)
    glColor3f(0.60, 0.70, 0.88)
    glVertex3f(left_outer_x, -L, 0)
    glVertex3f(left_outer_x, L, 0)
    glVertex3f(left_outer_x, L, wall_height)
    glVertex3f(left_outer_x, -L, wall_height)

    # ---------- Right wall (bluish) ----------
    glColor3f(0.70, 0.78, 0.92)
    right_outer_x = L
    right_inner_x = L - wall_thickness

    # Wall face (inner face visible from center)
    glVertex3f(right_inner_x, -L, 0)
    glVertex3f(right_inner_x, L, 0)
    glVertex3f(right_inner_x, L, wall_height)
    glVertex3f(right_inner_x, -L, wall_height)

    # Wall top
    glVertex3f(right_inner_x, -L, wall_height)
    glVertex3f(right_inner_x, L, wall_height)
    glVertex3f(right_outer_x, L, wall_height)
    glVertex3f(right_outer_x, -L, wall_height)

    # Wall outer face
    glColor3f(0.60, 0.70, 0.88)
    glVertex3f(right_outer_x, -L, 0)
    glVertex3f(right_outer_x, L, 0)
    glVertex3f(right_outer_x, L, wall_height)
    glVertex3f(right_outer_x, -L, wall_height)

    glEnd()


def idle():
    glutPostRedisplay()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glViewport(0, 0, 1000, 800)

    setupCamera()

    # Draw environment (green plane + road + walls)
    draw_environment()

    # Text overlay (kept from template)
    draw_text(10, 770, "Environment: green plane + road + bluish walls")
    draw_text(10, 740, f"Camera: {camera_pos} | fovY: {fovY}")

    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(1000, 800)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"3D Environment (Template Style)")

    glEnable(GL_DEPTH_TEST)  # IMPORTANT: depth on (your template clears depth buffer)

    glutDisplayFunc(showScreen)
    glutKeyboardFunc(keyboardListener)
    glutSpecialFunc(specialKeyListener)
    glutMouseFunc(mouseListener)
    glutIdleFunc(idle)

    glutMainLoop()


if __name__ == "__main__":
    main()
