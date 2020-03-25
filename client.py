import Pyro4

uri = input("URI Object? ").strip()

gererate_ticket = Pyro4.Proxy(uri)

answer="s"
while flag.lower() == "s":
    print(gerarate_ticket.new_ticket())
    answer = raw_input("Do you want to continue creating tickets? [Yes/No] ").strip()
