# Định nghĩa Class Csp: Biến, miền giá trị và ràng buộc
class Csp:
    def __init__(self, vars, domain_value, constraint):
        self.vars = vars
        self.domain_value = domain_value
        self.constraint = constraint
