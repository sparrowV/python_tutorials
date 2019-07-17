import unittest
import requests
def power(a,b):
    return a**b


class Test(unittest.TestCase):
    def test_power(self):
        res = power(2,4)
        self.assertEqual(res,16)

    def test_posts_len(self):
        response = requests.get("https://jsonplaceholder.typicode.com/posts",timeout = 0.1)
        if(response.ok):
            self.assertTrue(len(response.json()) == 100)
        else:
            self.fail("could not fetch data within %d second" % 1)



if __name__ == '__main_':
    unittest.main()








