from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'greeting': 'Hello world!'}

@view_config(route_name='timeline_json', renderer='json')
def timeline_json(request):
    return {
            "title": {
                "media": {
                  "url": "//www.flickr.com/photos/tm_10001/2310475988/",
                  "caption": "Timeline",
                  "credit": "flickr/<a href='http://www.flickr.com/photos/tm_10001/'>tm_10001</a>"
                },
                "text": {
                  "headline": "Whitney Houston<br/> 1963 - 2012",
                  "text": "<p>Houston's voice caught the imagination of the world propelling her to superstardom at an early age becoming one of the most awarded performers of our time. This is a look into the amazing heights she achieved and her personal struggles with substance abuse and a tumultuous marriage.</p>"
                }
            },
            "events": [
              {
                "media": {
                  "url": "{{ static_url }}/img/examples/houston/family.jpg",
                  "caption": "Houston's mother and Gospel singer, Cissy Houston (left) and cousin Dionne Warwick.",
                  "credit": "Cissy Houston photo:<a href='http://www.flickr.com/photos/11447043@N00/418180903/'>Tom Marcello</a><br/><a href='http://commons.wikimedia.org/wiki/File%3ADionne_Warwick_television_special_1969.JPG'>Dionne Warwick: CBS Television via Wikimedia Commons</a>"
                },
                "start_date": {
                  "month": "8",
                  "day": "9",
                  "year": "1963"
                },
                "text": {
                  "headline": "A Musical Heritage",
                  "text": "<p>Born in New Jersey on August 9th, 1963, Houston grew up surrounded by the music business. Her mother is gospel singer Cissy Houston and her cousins are Dee Dee and Dionne Warwick.</p>"
                }
              }
            ]
    }