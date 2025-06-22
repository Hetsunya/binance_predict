from dash import Dash
from app.logs.logger import setup_logger

from app.visual.components import create_layout
logger = setup_logger()
dash_app = Dash(__name__, assets_folder="../static")

dash_app.layout = create_layout()

def start_dash():
    print(dash_app.callback_map.keys())
    """Запуск сервера Dash"""
    try:
        dash_app.run(port=8050, host="localhost")
        logger.info("Dash server started")
    except Exception as e:
        logger.error(f"Dash server error: {e}")
        raise