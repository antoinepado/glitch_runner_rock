def extract_info(self):
    """Extracting information from info dict to class attributes"""

    # Extract dimension
    if "type" in self.info:
        type_data = self.info["type"]
        if "array_0d" in type_data:
            self.dimension = 0
        if "array_1d" in type_data:
            type_data = type_data.split("(")[1]
            type_data = type_data.split(")")[0]
            self.dimension = int(type_data)
        if "array_2d" in type_data:
            self.dimension = []
            type_string1 = type_data.split(",")[0]
            type_string1 = type_string1.split("(")[1]
            self.dimension.append(int(type_string1))

            type_string2 = type_data.split(",")[1]
            type_string2 = type_string2.split(")")[0]
            self.dimension.append(int(type_string2))
    else:
        raise NameError("No type in mccode data section!")

    # Extract component name
    if "component" in self.info:
        self.component_name = self.info["component"].rstrip()

    if "Parameters" in self.info:
        self.parameters = self.info["Parameters"]

    # Extract filename
    if "filename" in self.info:
        self.filename = self.info["filename"].rstrip()
    else:
        # Monitors without output files do exist
        #print("The component named \"" + self.component_name
        #      + "\" had no data file and will not be loaded.")
        self.filename = ""

    # Extract limits
    self.limits = []
    if "xylimits" in self.info:
        # find the four numbers xmin, xmax, ymin, ymax
        temp_str = self.info["xylimits"]
        limits_string = temp_str.split()
        for limit in limits_string:
            self.limits.append(float(limit))

    if "xlimits" in self.info:
        # find the two numbers, xmin, xmax
        temp_str = self.info["xlimits"]
        limits_string = temp_str.split()
        for limit in limits_string:
            self.limits.append(float(limit))

    # Extract plotting labels and title
    if "xlabel" in self.info:
        self.xlabel = self.info["xlabel"].rstrip()
    if "ylabel" in self.info:
        self.ylabel = self.info["ylabel"].rstrip()
    if "title" in self.info:
        self.title = self.info["title"].rstrip()

    if "values" in self.info:
        value_list = self.info["values"]
        value_list = value_list.strip().split(" ")
        self.total_I = float(value_list[0])
        self.total_E = float(value_list[1])
        self.total_N = float(value_list[2])

