#!/usr/bin/env python

import re

def isvalid(email):
    """chech email for validity"""
    pattern = re.compile(r"^([a-zA-Z0-9_\-]+)@([a-zA-Z0-9]+)\.\w{,3}$")
    return bool(pattern.match(email))
    
if __name__ == '__main__':
    n = int(input())
    emails = (input().strip() for _ in range(n))
    valid_emails = filter(isvalid, emails)
    print(sorted(valid_emails))