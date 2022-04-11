from pydantic import BaseSettings


class Configs(BaseSettings):
    database_url: str


configs = Configs()
print(configs)
