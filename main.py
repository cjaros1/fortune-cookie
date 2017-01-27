#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random

def getRandomFortune():
	fortunes=[
		"I see much code in your future",
		"Consider eating more fortune cookies",
		"You have tamed the mighty python, now you must free it onto the great spider's web"
	]
	return fortunes[random.randrange(len(fortunes)-1)]

class MainHandler(webapp2.RequestHandler):
    def get(self):
        fortune = getRandomFortune()
        header="<h1>Fortune Cookie</h1>"
        fortune_paragraph="<p>Your fortune: "+fortune+"</p>"
        lucky_number= random.randint(1,100)
        number_paragraph="<p>Your lucky number: " + str(lucky_number)+"</p>"
        self.response.write(header + fortune_paragraph + number_paragraph)

		

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
