import base64
import logging
import os

logger = logging.getLogger(__name__)


class Config:
    DEBUG = os.getenv("DEBUG", False)

    AUTH_USERNAME = os.environ.get("AUTH_USERNAME", "pi")
    AUTH_PASSWORD = os.environ.get("AUTH_PASSWORD")
    AUTH_BASE64 = base64.b64encode(
        "{}:{}".format(AUTH_USERNAME, AUTH_PASSWORD).encode("utf-8")
    )
    BASIC_AUTH = "Basic {}".format(AUTH_BASE64.decode("utf-8"))
    RESOLUTION = os.environ.get("RESOLUTION", "800x600").split("x")
    RESOLUTION_X = int(RESOLUTION[0])
    RESOLUTION_Y = int(RESOLUTION[1])
    FRAMERATE = int(os.environ.get("FRAMERATE", "24"))
    ROTATION = int(os.environ.get("ROTATE", 0))
    HFLIP = os.environ.get("HFLIP", "false").lower() == "true"
    VFLIP = os.environ.get("VFLIP", "false").lower() == "true"

    PAGE = """\
    <html>
    <head>
    <title>picamera MJPEG streaming demo</title>
    </head>
    <body>
    <h1>PiCamera MJPEG Streaming Demo</h1>
    <img src="stream.mjpg" width="{}" height="{}" />
    </body>
    </html>
    """.format(
        RESOLUTION_X, RESOLUTION_Y
    )

    def __init__(self):
        self.TV_BACKLIGHT_DEVICE_ID = self.get_secret("TV_BACKLIGHT_DEVICE_ID")
        self.PARTICLE_ACCESS_TOKEN = self.get_secret("PARTICLE_ACCESS_TOKEN")

    def get_secret(self, secret_name):
        secret_file = f"/run/secrets/{secret_name.lower()}"
        if os.path.exists(secret_file):
            logger.info(f"Reading {secret_name} from docker secrets")
            with open(secret_file, "r") as f:
                return f.readline().strip()
        else:
            logger.info(f"Reading {secret_name} from environment")
            return os.getenv(secret_name)
