from distutils.core import setup
setup(
  name = 'mz-invoicing',
  py_modules = ['mz_invoicing'],
  version = '0.1.0',
  description = 'Invoicing using InvoiceGenerator with database invoice list (using pyDAL)',
  install_requires = ['InvoiceGenerator', 'pyDAL'],
  author = 'Mirek Zvolsky',
  author_email = 'zvolsky@seznam.cz',
  url = 'https://github.com/zvolsky/mz-invoicing',
  download_url = 'https://github.com/zvolsky/mz-invoicing/tarball/0.1.0',
  keywords = ['invoice', 'invoicing'],
  classifiers=[
      'Development Status :: 4 - Beta',
      'Topic :: Office/Business :: Financial :: Accounting',
      'Intended Audience :: Developers',
      'Intended Audience :: Financial and Insurance Industry',
      'License :: OSI Approved :: BSD License',
      'Operating System :: OS Independent',
      'Programming Language :: Python',
      'Topic :: Software Development',
      'Programming Language :: Python :: 2',
  ],
)
