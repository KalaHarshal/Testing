class CallDetail:
    def __init__(self, calling_number, called_number, duration, call_type):
        self.calling_number = calling_number
        self.called_number = called_number
        self.duration = duration
        self.call_type = call_type

    def __str__(self):
        return "Calling Number: {}, Called Number: {}, Duration: {} mins, Call Type: {}".format(
            self.calling_number, self.called_number, self.duration, self.call_type)


class Util:
    def __init__(self):
        self.list_of_call_objects = None

    def parse_customer(self, list_of_call_string):
        self.list_of_call_objects = []
        
        for call in list_of_call_string:
            # Split each call string by comma to get the details
            details = call.split(',')
            # Create a CallDetail object and append to the list
            call_detail = CallDetail(details[0], details[1], details[2], details[3])
            self.list_of_call_objects.append(call_detail)

        # Print each CallDetail object
        for call_detail in self.list_of_call_objects:
            print call_detail


# Call strings data
call = '9990000001,9330000001,23,STD'
call2 = '9990000001,9330000002,54,Local'
call3 = '9990000001,9330000003,6,ISD'

# List of call strings
list_of_call_string = [call, call2, call3]

# Create an instance of Util and parse customer call details
util = Util()
util.parse_customer(list_of_call_string)
