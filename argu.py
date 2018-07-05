import sys

def main(argv):
    import getopt
    def usage():
        print('usage: %s [-u username] [-l limit]' % argv[0])
        return 100
    try:
        print(argv[1:])
        (opts, args) = getopt.getopt(argv[1:], 'u:l:')
    except getopt.GetoptError:
        print(getopt.GetoptError)
        return usage()
    if not args: return usage()
    twitter_screen_name = ""
    limit = 30
    for (k, v) in opts:
        if k == '-u': twitter_screen_name = str(v)
        elif k == '-l': limit = int(v)

    print(twitter_screen_name, limit)



if __name__ == '__main__':
    main(sys.argv)
    sys.exit()