from tortoise import Tortoise, run_async
from models import Profession, User
from pprint import PrettyPrinter
import json

pp = PrettyPrinter(indent=4)
db_on_disk = "sqlite://sqlite.db"
db_in_mem = "sqlite://:memory"


def open_file() -> json:
    file = open(
        "test_relations/random_data.json",
    )
    data = json.load(file)
    file.close()

    return data


async def main():
    await Tortoise.init(db_url=db_in_mem, modules={"models": ["__main__"]})
    await Tortoise.generate_schemas()

    data = open_file()

    for obj in data:

        profession = await Profession.get_or_create(name=obj["profession"])

        await User.get_or_create(
            name=f"{obj['firstname']} {obj['lastname']}",
            first_name=obj["firstname"],
            last_name=obj["lastname"],
            email=obj["email"],
            profession=profession[0],
        )

    output = await User.all().values()
    [pp.pprint(x) for x in output]


if __name__ == "__main__":
    run_async(main())
