from core.baseLoader import BaseLoaderClass
from core.config import DuspConfig
from dotenv import load_dotenv

load_dotenv()
config = DuspConfig({
})

loader = BaseLoaderClass(config)


def start():
    loader.load_modules()
    loader.run_all_modules()


if __name__ == "__main__":
    start()