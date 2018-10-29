import movie_svc


def main():
    print_header()
    search_event_loop()


def print_header():
    print("-----------------------------------")
    print("---------Movie Service App---------")
    print("-----------------------------------")


def search_event_loop():
    search = 'ONCE_THROUGH_LOOP'

    while search != 'x':
        try:
            search = input('Movie search text (x to exit): ')
            if search != 'x':
                results = movie_svc.find_movies(search)
                print("Found {} results.".format(len(results)))
                for r in results:
                    print('{} -- {}'.format(
                        r.year, r.title
                    ))
                print()
        except:
            print("YIKES that did not work!")

    print("Exiting ...")


if __name__ == '__main__':
    main()


