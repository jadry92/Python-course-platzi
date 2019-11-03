PASSWD = '12345'

def password_required(func):
    def wrapper():
        password = input('Cual es el passwd ?  ')

        if password == PASSWD:
            return func()
        else:
            print('error')
    return wrapper

def p_decorate(func):
   def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
   return func_wrapper

def strong_decorate(func):
    def func_wrapper(name):
        return "<strong>{0}</strong>".format(func(name))
    return func_wrapper

def div_decorate(func):
    def func_wrapper(name):
        return "<div>{0}</div>".format(func(name))
    return func_wrapper

def upper_dec(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        return result.upper()
    return wrapper

@upper_dec
def get_my_name(name):
   return "My name is {0}".format(name)

@div_decorate
@p_decorate
@strong_decorate
def get_text(name):
   return "lorem ipsum, {0} dolor sit amet".format(name)


a = get_text



@password_required
def needs_password():
    print('la contra esta correcta!!')

########################################################
## test general arguments "*args,**kwargs"
def test_valor_kwargs(**kwargs):
    if kwargs is not None:
        for key,  value in kwargs.items():
            print('%s == %s' %(key,value))

    print(type(kwargs))


def test_valor_args(n_arg, *args):
    print('primer valor normal: ', n_arg)
    for arg in args:
        print('este es un valor de *args: ',arg)
    print(type(args))


def test_valor_kwargs_args(*args, **kwargs):
    print(type(kwargs))
    print(kwargs)
    print('----------')
    print(type(args))
    print(args)

################################################################################
### example decorators in classes

def p_decorate_cla(func):
   def func_wrapper(*args, **kwargs):
       return "<p>{0}</p>".format(func(*args, **kwargs))
   return func_wrapper

class Person():
    def __init__(self):
        self.name = "John"
        self.family = "Doe"

    @p_decorate_cla
    def get_fullname(self):
        return self.name+" "+self.family


if __name__ == '__main__':
    #print(get_my_name('johan'))
    print(a('johan'))
    #test_valor_kwargs(caricatura='batman')
    #test_valor_args('carlos','Karla','Paola','Elena',[1,2,3,5,1])
    #test_valor_kwargs_args('flash', 'batman',[1,2,3,5,1], caricatura='batman', empresa = 'dc')
    #
    #my_person = Person()
    #print(my_person.get_fullname())
    #needs_password()
    #print(get_text('johan'))
