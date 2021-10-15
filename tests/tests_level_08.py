import hedy
import textwrap
from tests_level_01 import HedyTester

class TestsLevel8(HedyTester):
  level = 8
  
  def test_for_list(self):
    code = textwrap.dedent("""\
    dieren is hond, kat, papegaai
    for dier in dieren
      print dier""")

    result = hedy.transpile(code, self.level)

    expected = textwrap.dedent("""\
    dieren = ['hond', 'kat', 'papegaai']
    for dier in dieren:
      print(str(dier))""")

    self.assertEqual(expected, result.code)

  def test_for_list_multiple_lines(self):
    code = textwrap.dedent("""\
    familie is baby, mommy, daddy, grandpa, grandma
    for shark in familie
      print shark ' shark tudutudutudu'
      print shark ' shark tudutudutudu'
      print shark ' shark tudutudutudu'
      print shark ' shark'""")

    result = hedy.transpile(code, self.level)

    expected = textwrap.dedent("""\
    familie = ['baby', 'mommy', 'daddy', 'grandpa', 'grandma']
    for shark in familie:
      print(str(shark)+' shark tudutudutudu')
      print(str(shark)+' shark tudutudutudu')
      print(str(shark)+' shark tudutudutudu')
      print(str(shark)+' shark')""")

    self.assertEqual(expected, result.code)

