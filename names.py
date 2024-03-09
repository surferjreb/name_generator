

FIRST_NAMES = [
    'james', 'john', 'robert', 'michael', 'william',
    'david', 'richard', 'charles', 'joeseph', 'thomas',
    'christopher', 'daniel', 'paul', 'mark', 'donald',
    'george', 'ken', 'steven', 'brian', 'ron',
    'anthony', 'kevin', 'steven', 'ed', 'jason',
    'matt', 'gary', 'tim', 'jose', 'larry',
    'jeff', 'frank', 'scott', 'eric', 'stephen',
    'andrew', 'raymond', 'jack', 'gregory', 'joshua',
    'jerry', 'dennis', 'walter', 'pat', 'patrick',
    'peter', 'harold', 'geoff', 'doug', 'carl',
    'mary', 'patricia', 'barbara', 'linda', 'elizabeth',
    'maria', 'jennifer', 'susan', 'margaret', 'dorothy',
    'lisa', 'nancy', 'karen', 'betty', 'helen',
    'sandra', 'donna', 'ruth', 'sharon', 'michelle',
    'laura', 'sarah', 'kimberly', 'deborah', 'jessica',
    'shirley', 'cynthia', 'angela', 'emily', 'brenda',
    'amy', 'anna', 'rebecca', 'virginia', 'kathleen',
    'pamela', 'martha', 'debra', 'amanda', 'stephanie',
    'caroline', 'christine', 'marie', 'janet', 'catherine',
    'frances', 'ann', 'joyce', 'diana', 'alice',
    ]

LAST_NAMES = [
    'smith', 'johnson', 'williams', 'jones', 'brown',
    'davis', 'miller', 'wilson', 'moore', 'taylor',
    'anderson', 'thomas', 'jackson', 'white', 'harris',
    'martin', 'thompson', 'garcia', 'martinez', 'robinson',
    'clark', 'rodriguez', 'lewis', 'lee', 'walker',
    'hall', 'allen', 'young', 'hernandez', 'king',
    'wright', 'lopez', 'hill', 'scott', 'green',
    'adams', 'baker', 'gonzalez', 'nelson', 'carter',
    'mitchell', 'perez', 'roberts', 'turner', 'phillips',
    'campbell', 'parker', 'evans', 'edwards', 'collins',
    'stewart', 'sanchez', 'morris', 'rogers', 'reed',
    'cook', 'morgan', 'bell', 'murphy', 'bailey',
    'rivera', 'cooper', 'richardson', 'cox', 'howard',
    'ward', 'torres', 'peterson', 'gray', 'ramirez',
    'james', 'watson', 'brooks', 'kelly', 'sanders',
    'price', 'bennett', 'wood', 'barnes', 'ross',
    'henderson', 'coleman', 'jenkins', 'perry', 'powell',
    'long', 'patterson', 'hughes', 'flores', 'washington',
    'butler', 'simmons', 'foster', 'gonzales', 'bryant',
    'alexander', 'russell', 'griffin', 'diaz', 'hayes'
    ]

MIDDLE_NAMES = [
    ' ', 'alice', 'wren', 'rose', 'willow',
    'mae', 'sage', 'claire', 'nova', 'grace',
    'elizabeth', 'jane', 'margaret', 'rue', 'harper',
    'aria', 'briar', 'frances', 'elise', 'catherine',
    'faye', 'arden', 'jade', 'birdie', 'blythe',
    'june', 'fredrick', 'pearl', 'nyx', 'blair',
    'scout', 'ruth', 'alma', 'rain', 'mary',
    'indigo', 'neve', 'rae', 'avalon', 'gwen',
    'lennon', 'belle', 'lou', 'p', 'zora',
    'winter', 'coco', 'brooke', 'bea', 'echo',
    'lux', 'arya', ' ', 'h', 'paige',
    'raven', 'fleur', 'kate', 'reese', ' ',
    'anne', 'faith', 'maude', 'river',
    'joy', 'liv', 'kai', 'kit', 'tess',
    'fern', 'blue', 'dove', 'bee', 'venus',
    'marie', 'lark', 'reign', 'arcadia', 'peyton',
    'may', 'shea', 'alba', 'shay', 'sunny', 'james',
    'bree', 'moon', 'kennedy', 'zephyr', 'sierra',
    'ellen', 'lou', 'jean', 'india', 'maple',
    'rio', 'love', 'greer', 'bryn', 'joan',
    ]


class Names:
    '''

        The Names class is a storage and access class for the names list and
        the name values used to create the list values.

        .. autoclass::
          :methods:

    '''
    def __init__(self):
        self.names = []

    def get_names(self):
        '''
            Returns a list of names, this may be empty.

            :returns: list of name objects
            :rtype: list[Name]

        '''
        return self.names

    def add_name(self, name):
        try:
            if name is not None:
                self.names.append(name)
        except Exception:
            raise Exception('failed to add name')

    def __repr__(self):
        return 'names list'
