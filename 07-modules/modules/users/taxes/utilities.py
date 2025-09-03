if __name__ != "__main__":
    from ..management.management import save

    print(__name__)

    def payTaxes():
        print("User taxes paid")
        save()

if __name__ == "__main__":
    print("Task executed")