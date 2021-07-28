{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "from copy import deepcopy\n",
    "import pandas\n",
    "import os\n",
    "import json\n",
    "  \n",
    "# Folder Path\n",
    "path = 'python'\n",
    "\n",
    "def cross_join(left, right):\n",
    "    new_rows = [] if right else left\n",
    "    for left_row in left:\n",
    "        for right_row in right:\n",
    "            temp_row = deepcopy(left_row)\n",
    "            for key, value in right_row.items():\n",
    "                temp_row[key] = value\n",
    "            new_rows.append(deepcopy(temp_row))\n",
    "    return new_rows\n",
    "\n",
    "\n",
    "def flatten_list(data):\n",
    "    for elem in data:\n",
    "        if isinstance(elem, list):\n",
    "            yield from flatten_list(elem)\n",
    "        else:\n",
    "            yield elem\n",
    "\n",
    "\n",
    "def json_to_dataframe(data_in):\n",
    "    def flatten_json(data, prev_heading=''):\n",
    "        if isinstance(data, dict):\n",
    "            rows = [{}]\n",
    "            for key, value in data.items():\n",
    "                rows = cross_join(rows, flatten_json(value, prev_heading + '.' + key))\n",
    "        elif isinstance(data, list):\n",
    "            rows = []\n",
    "            for i in range(len(data)):\n",
    "                [rows.append(elem) for elem in flatten_list(flatten_json(data[i], prev_heading))]\n",
    "        else:\n",
    "            rows = [{prev_heading[1:]: data}]\n",
    "        return rows\n",
    "\n",
    "    return pandas.DataFrame(flatten_json(data_in))\n",
    "\n",
    "\n",
    "#if _name_ == '_main_':\n",
    "for file in os.listdir(path):\n",
    "# Check whether file is in json format or not\n",
    "    if file.endswith(\".json\"):\n",
    "        file_path = f\"{path}\\{file}\"\n",
    "\n",
    "    # call read json file function\n",
    "\n",
    "    with open(file_path) as json_file:\n",
    "        json_data = json.load(json_file)\n",
    "\n",
    "    df = json_to_dataframe(json_data)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
