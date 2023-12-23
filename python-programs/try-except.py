import sys


try:
    a = 1/1;
except ZeroDivisionError as e:
    print("zero division erro ====>>>")
except TypeError as e:
    print("zero division erro ====>>>")
except Exception as e:
    print("Exception ", e)
    sys.exit()
else:
    print("NO Exception")
finally:
    print("Will execute always")
