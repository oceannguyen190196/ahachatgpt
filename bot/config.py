import yaml
import dotenv
from pathlib import Path

config_dir = Path(__file__).parent.parent.resolve() / "config"

# load yaml config
with open(config_dir / "config.yml", 'r') as f:
    config_yaml = yaml.safe_load(f)

# load .env config
config_env = dotenv.dotenv_values(config_dir / "config.env")

# config parameters
telegram_token = config_yaml["6218475791:AAFH0WdVkZaHZZGbITR0v5DFFgo7w_xH4v0"]
openai_api_key = config_yaml["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"]
allowed_telegram_usernames = config_yaml["allowed_telegram_usernames"]
new_dialog_timeout = config_yaml["new_dialog_timeout"]
mongodb_uri = f"mongodb://mongo:{config_env['MONGODB_PORT']}"
