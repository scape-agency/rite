# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Case Class
===================

Todo:
-----

Links:
------

"""


# =============================================================================
# Import
# =============================================================================

# Import | Futures

# Import | Standard Library
import os
import uuid
import os, shutil, glob
import ntpath
from datetime import date
import json
import shutil
from collections import defaultdict
import unicodedata
import re

# Import | Libraries

# Import | Local Modules


# =============================================================================
# Functions
# =============================================================================

def delete_contents(folder):
    """
    """
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))



def create_date_dict():
    """
    """
    date_dict = {}
    date_today = date.today()
    date_default = str(date_today)
    date_dict['date_year'] = date_today.year
    date_dict['date_default'] = date_default
    date_dict['date_us_simple'] = date_default.replace("-","/")
    return(date_dict)



def create_uuid_random():
    """
    """
# make a random UUID
    id = uuid.uuid4()
    return id

def create_uuid_hex():
    """
    """
# Convert a UUID to a string of hex digits in standard form
    id = str(uuid.uuid4())
    return id

def create_uuid_hex32():
    """
    Convert a UUID to a string of hex digits in standard form
    """
    id = uuid.uuid4().hex
    return id


def create_slug(value, allow_unicode=False):
    """
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')

def create_slug_snake(value, allow_unicode=False):
    """
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '_', value).strip('-_')


def slugify(value, allow_unicode=False):
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')




def etree_to_dict(t):
    """
    """
    d = {t.tag: {} if t.attrib else None}
    children = list(t)
    if children:
        dd = defaultdict(list)
        for dc in map(etree_to_dict, children):
            for k, v in dc.items():
                dd[k].append(v)
        d = {t.tag: {k:v[0] if len(v) == 1 else v for k, v in dd.items()}}
    if t.attrib:
        d[t.tag].update(('@' + k, v) for k, v in t.attrib.items())
    if t.text:
        text = t.text.strip()
        if children or t.attrib:
            if text:
              d[t.tag]['#text'] = text
        else:
            d[t.tag] = text
    return d


# Function | Create Directory
def create_dir(dir_path, mode=777):
    """
    """
    if not os.path.exists(dir_path):
        # os.mkdir(dir_path)
        try:
            os.makedirs(dir_path, mode)
        except OSError as err:
            return err
    else:
        pass


# Function | Write Template
def write_template(environment, context, template, export_path):
    """
    """
    template = environment.get_template(template)
    with open(export_path, 'w') as fh:
        fh.write(template.render(context))



def list_dirs(rootdir):
    """
    """
    dirs = []
    for file in os.listdir(rootdir):
        d = os.path.join(rootdir, file)
        if os.path.isdir(d):
            dirs.append(file)
    return(dirs)

 

def copy_file(src, dst):
    """
    """
    shutil.copyfile(src, dst)


def list_files(rootdir):
    """
    """
    dirs = []
    for file in os.listdir(rootdir):
        d = os.path.join(rootdir, file)
        dirs.append(file)
    return(dirs)



def copy_files(source_dir, target_dir):
    """
    """
    file_names = os.listdir(source_dir)
        
    for file_name in file_names:
        # shutil.move(os.path.join(source_dir, file_name), target_dir)
        source = os.path.join(source_dir, file_name)
        target = os.path.join(target_dir, file_name)
        # print(source)
        # print(target)
        shutil.copyfile(source, target)


def copy_all_files(source_dir, target_dir):
    """
    """
    for root, dirs, files in os.walk(source_dir):  # replace the . with your starting directory

        for file in files:
            path_file = os.path.join(root,file)
            shutil.copy2(path_file,target_dir) # change you destination dir
            # shutil.copy2(path_file,os.path.join(rootdir, file)) # change you destination dir



def path_leaf(path):
    """
    """
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)



def load_json(file):
    """
    """
    with open(file) as f:
        dict = json.load(f)
        return(dict)