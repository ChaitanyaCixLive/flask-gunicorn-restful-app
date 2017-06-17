#! -*- coding=utf-8 -*-


from exceptions import RuntimeError


class CustomerException(RuntimeError):

    def __init__(self, msg):
        self.args = msg


class OtherException(RuntimeError):

    def __init__(self, msg):
        self.args = msg



if __name__ == '__main__':
    try:
        raise CustomerException('customer exception raise...')
        # raise OtherException('other exception raise...')
    except CustomerException,e:
        print e
        print str("".join(e.args))
    except Exception:
        print 'execute error'
    finally:
        print '---final---'

    print '-----end-------'
