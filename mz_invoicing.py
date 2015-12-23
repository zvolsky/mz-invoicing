#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Python lib for Invoicing using InvoiceGenerator with database invoices list (using pyDAL)
install_requires = ['InvoiceGenerator', 'pyDAL']

Usage:
  import mz_invoices
"""

from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator, Address
from InvoiceGefrom InvoiceGenerator.pdf import SimpleInvoice
from pydal import DAL, Field

if __name__ == "__main__":
    provider = Address()
    provider.firstname = "Miroslav"
    provider.lastname = "Zvolský"
    provider.address = "Dačického 7"
    provider.city = "Praha 4"
    provider.zip = "140 00"
    provider.phone = "+420732457966"
    provider.email = "zvolsky@seznam.cz"
    provider.bank_name = "FIO"
    provider.bank_account = "2600307929/2010"
    provider.note = "IČO: 71883797"

    client = Address()
    client.firstname = "Adam"
    client.lastname = "Štrauch"
    client.address = "Houští 474"
    client.city = "Lanškroun"
    client.zip = "563 01"
    client.phone = "+420777636388"
    client.email = "cx@initd.cz"
    client.bank_name = "GE Money Bank"
    client.bank_account = "181553009/0600"
    client.note = "Blablabla"

    item1 = Item()
    item1.name = "Položka 1"
    item1.count = 5
    item1.price = 100
    item2 = Item()
    item2.name = "Položka 2"
    item2.count = 10
    item2.price = 750

    invoice = Invoice()
    invoice.setClient(client)
    invoice.setProvider(provider)
    invoice.setTitle("Faktura")
    invoice.setVS("00001")
    invoice.setCreator("Adam Štrauch")
    invoice.addItem(item1)
    invoice.addItem(item2)

    f = open("test.pdf", "w")
    f.write(invoice.getContent())
    f.close()
