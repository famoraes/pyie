# -*- coding: utf-8 -*-

from pyie import config

class ValideStateInscription(object):

    def __init__(self, *args, **kwargs):
        self.state = kwargs['state']
        self.state_inscription = kwargs['state_inscription']

        self.state_parameters = config.STATES_CONFIGS
        self.states = config.STATES

    def validate_state_inscription(self):
        if (self.state and not self.state_inscription or
            not self.state and not self.state_inscription or
            self.state_inscription.upper() == config.FREE_TERM):

            return True
        elif self.state in self.states:

            return self.ie_param()
        elif hasattr(self, "ie_%s" % self.state.lower()):

            return getattr(self, "ie_%s" % self.state.lower())()

        return False

    def ie_param(self):
        size = self.states_configs[self.state].get('size', 0)
        state_inscription = unicode(self.state_inscription).strip()
        state_inscription = re.sub('[^0-9]', '', state_inscription)
        value_size = self.states_configs[self.state].get('value_size', size - 1)
        starts_with = self.states_configs[self.state].get('starts_with', '')
        state_inscription_int = [int(c) for c in state_inscription]
        new_state_inscription = state_inscription_int[:value_size]
        prod = self.states_configs[self.state].get(
            'prod', [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2])
        prod = prod[-value_size:]

        if not len(state_inscription) == size:
            return False

        if not state_inscription.startswith(starts_with):
            return False

        while len(new_state_inscription) < size:
            r = sum([x * y for (x, y) in zip(new_state_inscription, prod)]) % \
                self.states_configs[self.state].get('div', 11)

            if r > 1:
                f = 11 - r
            else:
                f = 0

            if not self.state in ['RR']:
                new_state_inscription.append(f)
            else:
                new_state_inscription.append(r)
            prod.insert(0, prod[0] + 1)

        if not new_state_inscription == state_inscription_int:
            return False

        return True

    def ie_ap(self):
        state_inscription = re.sub('[^0-9]', '', self.state_inscription)

        # verificando o tamanho da inscrição estadual
        if len(state_inscription) != 9:
            return False

        # verificando os dois primeiros dígitos
        if not state_inscription.startswith('03'):
            return False

        # Pega apenas os 8 primeiros dígitos da inscrição estadual e
        # define os valores de 'p' e 'd'
        state_inscription_int = int(state_inscription[:8])
        if state_inscription_int <= 3017000:
            inscr_est_p = 5
            inscr_est_d = 0
        elif state_inscription_int <= 3019022:
            inscr_est_p = 9
            inscr_est_d = 1
        else:
            inscr_est_p = 0
            inscr_est_d = 0

        # Pega apenas os 8 primeiros dígitos da inscrição estadual e
        # gera o dígito verificador
        state_inscription = map(int, state_inscription)
        new_state_inscription = state_inscription[:8]

        prod = [9, 8, 7, 6, 5, 4, 3, 2]
        r = (inscr_est_p + sum([x * y for (x, y) in zip(
            new_state_inscription, prod)])) % 11
        if r > 1:
            f = 11 - r
        elif r == 1:
            f = 0
        else:
            f = inscr_est_d
        new_state_inscription.append(f)

        if not new_state_inscription == state_inscription:
            return False

        return True

    def ie_ba(self):
        state_inscription = re.sub('[^0-9]', '', self.state_inscription)
        state_inscription = map(int, state_inscription)

        # verificando o tamanho da inscrição estadual
        if len(state_inscription) == 8:
            size = 8
            value_size = 6
            test_digit = 0
        elif len(state_inscription) == 9:
            size = 9
            value_size = 7
            test_digit = 1
        else:
            return False

        new_state_inscription = state_inscription[:value_size]

        prod = [8, 7, 6, 5, 4, 3, 2][-value_size:]

        if state_inscription[test_digit] in [0, 1, 2, 3, 4, 5, 8]:
            modulo = 10
        else:
            modulo = 11

        while len(new_state_inscription) < size:
            r = sum([x * y for (x, y) in zip(
                new_state_inscription, prod)]) % modulo
            if r > 0:
                f = modulo - r
            else:
                f = 0

            if f >= 10 and modulo == 11:
                f = 0

            if len(new_state_inscription) == value_size:
                new_state_inscription.append(f)
            else:
                new_state_inscription.insert(value_size, f)
            prod.insert(0, prod[0] + 1)

        if not new_state_inscription == state_inscription:
            return False

        return True

    def ie_go(self):
        state_inscription = re.sub('[^0-9]', '', self.state_inscription)

        # verificando o tamanho da inscrição estadual
        if len(state_inscription) != 9:
            return False

        # verificando os dois primeiros dígitos
        if not state_inscription[:2] in ['10', '11', '15']:
            return False

        # Pega apenas os 8 primeiros dígitos da inscrição estadual e
        # define os valores de 'p' e 'd'
        state_inscription_int = int(state_inscription[:8])
        if (state_inscription_int >= 10103105 and
            state_inscription_int <= 10119997):
            inscr_est_d = 1
        else:
            inscr_est_d = 0

        # Pega apenas os 8 primeiros dígitos da inscrição estadual e
        # gera o dígito verificador
        state_inscription = map(int, state_inscription)
        new_state_inscription = state_inscription[:8]

        prod = [9, 8, 7, 6, 5, 4, 3, 2]
        r = sum([x * y for (x, y) in zip(new_state_inscription, prod)]) % 11
        if r > 1:
            f = 11 - r
        elif r == 1:
            f = inscr_est_d
        else:
            f = 0
        new_state_inscription.append(f)

        if not new_state_inscription == state_inscription:
            return False

        return True


    def ie_mg(self):
        state_inscription = re.sub('[^0-9]', '', self.state_inscription)

        # verificando o tamanho da inscrição estadual
        if len(state_inscription) != 13:
            return False

        # Pega apenas os 11 primeiros dígitos da inscrição estadual e
        # gera os dígitos verificadores
        state_inscription = map(int, state_inscription)
        new_state_inscription = state_inscription[:11]

        new_state_inscription_aux = list(new_state_inscription)
        new_state_inscription_aux.insert(3, 0)
        prod = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
        r = str([x * y for (x, y) in zip(new_state_inscription_aux, prod)])
        r = re.sub('[^0-9]', '', r)
        r = map(int, r)
        r = sum(r)
        r2 = (r / 10 + 1) * 10
        r = r2 - r

        if r >= 10:
            r = 0

        new_state_inscription.append(r)

        prod = [3, 2, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
        r = sum([x * y for (x, y) in zip(new_state_inscription, prod)]) % 11
        if r > 1:
            f = 11 - r
        else:
            f = 0
        new_state_inscription.append(f)

        if not new_state_inscription == state_inscription:
            return False

        return True

    def ie_pe(self):
        state_inscription = re.sub('[^0-9]', '', self.state_inscription)

        # verificando o tamanho da inscrição estadual
        if (len(state_inscription) != 9) and (len(state_inscription) != 14):
            return False

        state_inscription = map(int, state_inscription)

        # verificando o tamanho da inscrição estadual
        if len(state_inscription) == 9:

            # Pega apenas os 7 primeiros dígitos da inscrição estadual e
            # gera os dígitos verificadores
            state_inscription = map(int, state_inscription)
            new_state_inscription = state_inscription[:7]

            prod = [8, 7, 6, 5, 4, 3, 2]
            while len(new_state_inscription) < 9:
                r = sum([x * y for (x, y) in zip(
                    new_state_inscription, prod)]) % 11
                if r > 1:
                    f = 11 - r
                else:
                    f = 0
                new_state_inscription.append(f)
                prod.insert(0, 9)
        elif len(state_inscription) == 14:

            # Pega apenas os 13 primeiros dígitos da inscrição estadual e
            # gera o dígito verificador
            state_inscription = map(int, state_inscription)
            new_state_inscription = state_inscription[:13]

            prod = [5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2]
            r = sum([x * y for (x, y) in zip(new_state_inscription, prod)]) % 11
            f = 11 - r
            if f > 10:
                f = f - 10
            new_state_inscription.append(f)

        if not new_state_inscription == state_inscription:
            return False

        return True


    def ie_ro(self):
        def gera_digito_ro(new_state_inscription, prod):
            r = sum([x * y for (x, y) in zip(new_state_inscription, prod)]) % 11
            f = 11 - r
            if f > 9:
                f = f - 10
            return f

        state_inscription = re.sub('[^0-9]', '', self.state_inscription)
        state_inscription = map(int, state_inscription)

        # verificando o tamanho da inscrição estadual
        if len(state_inscription) == 9:
            # Despreza-se os 3 primeiros dígitos, pega apenas os 8 primeiros
            # dígitos da inscrição estadual e gera o dígito verificador
            new_state_inscription = state_inscription[3:8]

            prod = [6, 5, 4, 3, 2]
            f = gera_digito_ro(new_state_inscription, prod)
            new_state_inscription.append(f)

            new_state_inscription = \
                state_inscription[0:3] + new_state_inscription
        elif len(state_inscription) == 14:
            # Pega apenas os 13 primeiros dígitos da inscrição estadual e
            # gera o dígito verificador
            new_state_inscription = state_inscription[:13]

            prod = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
            f = gera_digito_ro(new_state_inscription, prod)
            new_state_inscription.append(f)
        else:
            return False

        if not new_state_inscription == state_inscription:
            return False

        return True


    def ie_sp(self):
        def gera_digito_sp(new_state_inscription, prod, state_inscription):
            r = sum([x * y for (x, y) in zip(new_state_inscription, prod)]) % 11
            if r < 10:
                return r
            elif r == 10:
                return 0
            else:
                return 1

        # Industriais e comerciais
        if self.state_inscription[0] != 'P':

            state_inscription = re.sub('[^0-9]', '', self.state_inscription)

            # verificando o tamanho da inscrição estadual
            if len(state_inscription) != 12:
                return False

            # Pega apenas os 8 primeiros dígitos da inscrição estadual e
            # gera o primeiro dígito verificador
            state_inscription = map(int, state_inscription)
            new_state_inscription = state_inscription[:8]

            prod = [1, 3, 4, 5, 6, 7, 8, 10]
            f = gera_digito_sp(new_state_inscription, prod, state_inscription)
            new_state_inscription.append(f)

            # gera o segundo dígito verificador
            new_state_inscription.extend(state_inscription[9:11])
            prod = [3, 2, 10, 9, 8, 7, 6, 5, 4, 3, 2]
            f = gera_digito_sp(new_state_inscription, prod, state_inscription)
            new_state_inscription.append(f)

        # Produtor rural
        else:
            state_inscription = re.sub('[^0-9]', '', self.state_inscription)

            # verificando o tamanho da inscrição estadual
            if len(state_inscription) != 12:
                return False

            # verificando o primeiro dígito depois do 'P'
            if state_inscription[0] != '0':
                return False

            # Pega apenas os 8 primeiros dígitos da inscrição estadual e
            # gera o dígito verificador
            state_inscription = map(int, state_inscription)
            new_state_inscription = state_inscription[:8]

            prod = [1, 3, 4, 5, 6, 7, 8, 10]
            f = gera_digito_sp(new_state_inscription, prod, state_inscription)
            new_state_inscription.append(f)

            new_state_inscription.extend(state_inscription[9:])

        if not new_state_inscription == state_inscription:
            return False

        return True

    def ie_to(self):
        state_inscription = re.sub('[^0-9]', '', self.state_inscription)

        # verificando o tamanho da inscrição estadual
        if len(state_inscription) != 11:
            return False

        # verificando os dígitos 3 e 4
        if not state_inscription[2:4] in ['01', '02', '03', '99']:
            return False

        # Pega apenas os dígitos que entram no cálculo
        state_inscription = map(int, state_inscription)
        new_state_inscription = state_inscription[:2] + state_inscription[4:10]

        prod = [9, 8, 7, 6, 5, 4, 3, 2]
        r = sum([x * y for (x, y) in zip(new_state_inscription, prod)]) % 11
        if r > 1:
            f = 11 - r
        else:
            f = 0
        new_state_inscription.append(f)

        new_state_inscription = new_state_inscription[:2] + \
            state_inscription[2:4] + new_state_inscription[2:]

        if not new_state_inscription == state_inscription:
            return False

        return True