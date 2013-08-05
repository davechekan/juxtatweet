from flask.ext.classy import FlaskView
from flask import request

import datetime

import werkzeug.exceptions as exc

import juxtapy
import juxtapy.model as model

from juxtapy.utils.decorators import jsonify

class JuxtaView(FlaskView):

    @jsonify
    def get(self, id):
        """
        Load and return data about a single juxta.
        """
        juxta = self._get_juxta(id)
        return juxta.to_dict()

    @jsonify
    def query(self):
        """
        FIXME: Specify search parameters.
        """
        return []

    @jsonify
    def post(self):
        """
        Create a juxta.
        """
        params = self._get_create_params()

        juxta = model.Juxta(**params)

        juxtapy.db.session.add(juxta)
        juxtapy.db.session.commit()

        return juxta.to_dict()

    @jsonify
    def delete(self, id):
        """
        Set a juxta to deleted.
        """
        juxta = self._get_juxta(id)

        juxta.deleted = True
        juxta.deleted_date = datetime.datetime.utcnow()

        juxtapy.db.session.commit()

        return True

    #######################################################
    #################### PRIVATE BELOW ####################
    #######################################################

    def _get_juxta(self, id):
        """
        Find the juxta by id, raise NotFound if we couldn't find it.
        """
        juxta = model.Juxta.query.filter(model.Juxta.id == id)  \
                                 .filter(~model.Juxta.deleted)  \
                                 .first()

        if not juxta:
            msg = 'Nothing by that id here - %s' % id
            raise exc.NotFound(msg)

        return juxta

    def _get_create_params(self):
        """
        Ensure we have all necessary parameters to create a juxta.
        """
        params = self._get_all_possible_params()
        required = ('tweet_url', 'image_url', )

        missing = [req for req in required if req not in params or params[req] is None]

        if missing:
            msg = 'Missing required args: %s' % missing.join(',')
            raise exc.Forbidden(msg)

        return params

    def _get_all_possible_params(self):
        """
        Snatch all possible params for a juxta out of the request.
        """
        possible_params = ('tweet_url', 'image_url', )
        return { p : request.values.get(p) for p in possible_params }
