def convert(self):
    data=self.__dict__
    data.pop("_sa_instance_state")
    return data