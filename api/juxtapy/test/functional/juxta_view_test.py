import juxtapy
import juxtapy.model as model

from test_base import JuxtapyTestCase

import constants

class JuxtaViewTest(JuxtapyTestCase):

    def test_create_juxta(self):
        """
        Test successfully creating a juxta object
        """

        tweet_url = 'http://mytweeturl.com'
        image_url = 'http://myimage.com'

        post_data = {
            'tweet_url' : tweet_url,
            'image_url' : image_url,
        }

        ret = self.client.post(path=constants.juxta_url, data=post_data)

        juxta = ret.json

        self.assertTrue(juxta['id']       is not None)
        self.assertTrue(juxta['created']  is not None)
        self.assertTrue(juxta['modified'] is not None)

        self.assertEqual(juxta['tweet_url'], tweet_url)
        self.assertEqual(juxta['image_url'], image_url)

    def test_get_juxta(self):

        tweet_url = u'http://mytweeturl.com'
        image_url = u'http://myimage.com'

        args = {
            'tweet_url' : tweet_url,
            'image_url' : image_url,
        }

        juxta_obj = model.Juxta(**args)

        juxtapy.db.session.add(juxta_obj)
        juxtapy.db.session.commit()

        path = '%s%s' % (constants.juxta_url, juxta_obj.id)

        ret = self.client.get(path=path)

        juxta = ret.json

        self.assertEqual(juxta['id'], juxta_obj.id)
        self.assertEqual(juxta['tweet_url'], juxta_obj.tweet_url)
        self.assertEqual(juxta['image_url'], juxta_obj.image_url)
