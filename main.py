from core import BaseLoaderClass, DuspConfig
from dotenv import load_dotenv

load_dotenv()
config = DuspConfig({
})

loader = BaseLoaderClass(config)


def start():
    loader.load_modules()
    loader.run_all_modules()
    input("Press enter to stop...")
    loader.unload_modules()


if __name__ == "__main__":
    start()