class SwagFormatter(object):
    def format(self, swag):
        if swag == None:
            return 
        output = ''
        for i in range(len(swag) - 1):
            output += "{0}, ".format(swag[i])
        output += "{0}.".format(swag[len(swag) - 1])
        return output
