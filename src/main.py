from lib import load_data

def main() -> None:
    dataloader = load_data.DataLoader("../data/fake_test_data.csv", "../conf/default_room_dict.json")
    dataloader.load_CSV()
    dataloader.load_JSON()
    print(dataloader.get_CSV())
    print(dataloader.get_JSON())

if __name__ == "__main__":
    main()