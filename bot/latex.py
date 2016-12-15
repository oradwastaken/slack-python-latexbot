import requests
import string
import sys
import urllib

QUICKLATEX_URL = 'http://quicklatex.com/latex3.f'

class LatexUtility(object):
  def request_QuickLatex(_, latex_string):
    print >> sys.stderr, "Rendering %s on QuickLaTeX..." % latex_string
    latex_string = '\\[ %s \\]' % latex_string
    data = {
      'formula': latex_string,
      'fsize': '20px',
      'fcolor': '000000',
      'mode': '0',
      'out': '1',
      # 'remhost': 'quicklatex.com',
      'preamble': "\\usepackage{amsmath,amsfonts,amsthm,amssymb}",
    }

    response = requests.post(QUICKLATEX_URL,
                             data=urllib.urlencode(data).replace('+', '%20'))
    if response.status_code != 200:
      return

    image_url = response.text.split()[1]
    return image_url