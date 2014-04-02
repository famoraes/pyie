# -*- coding: utf-8 -*-

FREE_TERM = 'ISENTO'

STATES = ('AC', 'AL', 'AM', 'CE', 'DF', 'ES', 'MA', 'MT', 'MS', 'PA', 'PB',
            'PR', 'PI', 'RJ', 'RN', 'RS', 'RR'  , 'SC', 'SE')

STATES_CONFIGS = {
    'AC': {
        'size': 13,
        'value_size': 11,
        'starts_with': '01'
    },
    'AL': {
        'size': 9,
        'starts_with': '24'
    },
    'AM': {
        'size': 9
    },
    'CE': {
        'size': 9
    },
    'DF': {
        'size': 13,
        'value_size': 11,
        'starts_with': '07'
    },
    'ES': {
        'size': 9
    },
    'MA': {
        'size': 9,
        'starts_with': '12'
    },
    'MT': {
        'size': 11,
        'prod': [3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    },
    'MS': {
        'size': 9,
        'starts_with': '28'
    },
    'PA': {
        'size': 9,
        'starts_with': '15'
    },
    'PB': {
        'size': 9
    },
    'PR': {
        'size': 10,
        'value_size': 8,
        'prod': [3, 2, 7, 6, 5, 4, 3, 2]
    },
    'PI': {
        'size': 9
    },
    'RJ': {
        'size': 8,
        'prod': [2, 7, 6, 5, 4, 3, 2]
    },
    'RN': {
        'size': 10,
        'value_size': 9,
        'prod': [10, 9, 8, 7, 6, 5, 4, 3, 2]
    },
    'RS': {
        'size': 10
    },
    'RR': {
        'size': 9,
        'starts_with': '24',
        'prod': [1, 2, 3, 4, 5, 6, 7, 8],
        'div': 9
    },
    'SC': {
        'size': 9
    },
    'SE': {
        'size': 9
    }
}
