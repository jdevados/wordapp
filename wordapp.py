
import cgi 
import os 
import random
import logging


from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.api import memcache
from google.appengine.api.labs import taskqueue

class ISEEVocabulary(db.Model):
    id= db.IntegerProperty
    wrd = db.StringProperty(multiline=True)
    defn = db.StringProperty(multiline=True)

class MainPage(webapp.RequestHandler):

                                 
    def get(self):

       
        #words=self.init_words() 
        #randid=random.randrange(1,502)
        #resultset = db.GqlQuery("SELECT * FROM ISEEVocabulary")

        #template_values = {
        #   'word':resultset[randid]
        #    }

        #path = os.path.join(os.path.dirname(__file__), 'index.html')
        #self.response.out.write(template.render(path, template_values))

        taskqueue.add(url='/queue', params={})
        path = os.path.join(os.path.dirname(__file__), 'firstpage.html')
        self.response.out.write(template.render(path, {}))

class QueuePage(webapp.RequestHandler):


    def init_words(self):
        newword=ISEEVocabulary(id=1, wrd="capricious", defn="fickle, impulsive, unpredictable")
        newword.put();
        newword=ISEEVocabulary(id=2, wrd="endorse", defn="to show approval")
        newword.put();
        newword=ISEEVocabulary(id=3, wrd="insinuate", defn="to indirectly suggest something not credible")
        newword.put();

        newword=ISEEVocabulary(id=4, wrd="innate", defn="inborn, natural")
        newword.put();
        newword=ISEEVocabulary(id=5, wrd="inhibit", defn="to restrain or supress")
        newword.put();

        newword=ISEEVocabulary(id=6, wrd="beguile", defn="to deceive")
        newword.put();

        newword=ISEEVocabulary(id=7, wrd="convene", defn="to meet; to come together")
        newword.put();

        newword=ISEEVocabulary(id=8, wrd="fervent", defn="intense, passionate")
        newword.put();
        newword=ISEEVocabulary(id=9, wrd="entourage", defn="a group of associates or attendants")
        newword.put();
        newword=ISEEVocabulary(id=10, wrd="essential", defn="necessary")
        newword.put();
        newword=ISEEVocabulary(id=11, wrd="adverse", defn="unfavorable, bringing harm")
        newword.put();
        newword=ISEEVocabulary(id=12, wrd="decree", defn="unofficial order or decision")
        newword.put();
        newword=ISEEVocabulary(id=13, wrd="impasse", defn="blocked path, deadlock")
        newword.put();

        newword=ISEEVocabulary(id=14, wrd="ardent", defn="passionate")
        newword.put();
        newword=ISEEVocabulary(id=15, wrd="trepidation", defn="fear, apprehension")
        newword.put();
        newword=ISEEVocabulary(id=16, wrd="zealous", defn="filled with eagerness, fervor or passion")
        newword.put();
        newword=ISEEVocabulary(id=17, wrd="synopsis", defn="a summary")
        newword.put();
        newword=ISEEVocabulary(id=18, wrd="prolific", defn="abundant, plentiful")
        newword.put();
        newword=ISEEVocabulary(id=19, wrd="brusque", defn="abrupt")
        newword.put();
        newword=ISEEVocabulary(id=20, wrd="peddle", defn="to sell or offer goods from place to place")
        newword.put();
        newword=ISEEVocabulary(id=21, wrd="contentious", defn="quarrelsome; argumentative")
        newword.put();
        newword=ISEEVocabulary(id=22, wrd="wrath", defn="anger, indignation")
        newword.put();
        newword=ISEEVocabulary(id=23, wrd="deceit", defn="a lie")
        newword.put();

        newword=ISEEVocabulary(id=24, wrd="felicitous", defn="pleasing")
        newword.put();
                          
        newword=ISEEVocabulary(id=25, wrd="repugnant", defn="loathsome, hateful")
        newword.put();

        newword=ISEEVocabulary(id=26, wrd="plausible", defn="believable, seemingly acceptable")
        newword.put();
        newword=ISEEVocabulary(id=27, wrd="heterogeneous", defn="composed of dissimilar parts; diverse")
        newword.put();
        newword=ISEEVocabulary(id=28, wrd="plight", defn="an unfortunate, difficult situation; a predicament")
        newword.put();
        newword=ISEEVocabulary(id=29, wrd="bravado", defn="pretended courage or feigned confidence")
        newword.put();
        newword=ISEEVocabulary(id=30, wrd="writhe", defn="to twist one's body continuously (in pain); to suffer because of")
        newword.put();

        newword=ISEEVocabulary(id=31, wrd="emulate", defn="to imitiate, to copy, to mimic")
        newword.put();
        newword=ISEEVocabulary(id=32, wrd="deluge", defn="a great flood")
        newword.put();
        newword=ISEEVocabulary(id=33, wrd="perjury", defn="to lie under oath")
        newword.put();
        newword=ISEEVocabulary(id=34, wrd="obese", defn="very fat")
        newword.put();
        newword=ISEEVocabulary(id=35, wrd="despondent", defn="dejected; discouraged")
        newword.put();
        newword=ISEEVocabulary(id=36, wrd="debunk", defn="to discredit")
        newword.put();

        newword=ISEEVocabulary(id=37, wrd="reminiscence", defn="remembrance of past events")
        newword.put();
        newword=ISEEVocabulary(id=38, wrd="palatable", defn="pleasant to the taste; acceptable; welcome")
        newword.put();
        newword=ISEEVocabulary(id=39, wrd="deplore", defn="to express disapproval")
        newword.put();
        newword=ISEEVocabulary(id=40, wrd="rudimentary", defn="undeveloped; elementary")
        newword.put();
        newword=ISEEVocabulary(id=41, wrd="deficient", defn="lacking; incomplete")
        newword.put();
        newword=ISEEVocabulary(id=42, wrd="rout", defn="complete defeat")
        newword.put();
        newword=ISEEVocabulary(id=43, wrd="delude", defn="to mislead; to deceive")
        newword.put();
        newword=ISEEVocabulary(id=44, wrd="obsolete", defn="no longer in use")
        newword.put();
        newword=ISEEVocabulary(id=45, wrd="devastate", defn="to lay waste; to destroy; to overwhelm")
        newword.put();
        newword=ISEEVocabulary(id=46, wrd="fatigue", defn="exhaustion; weariness; extreme tiredness")
        newword.put();
        newword=ISEEVocabulary(id=47, wrd="destitute", defn="very poor")
        newword.put();
        newword=ISEEVocabulary(id=48, wrd="brevity", defn="conciseness; briefness")
        newword.put();
        newword=ISEEVocabulary(id=49, wrd="judicious", defn="demonstrating good judgement; sensible")
        newword.put();
        newword=ISEEVocabulary(id=50, wrd="succumb", defn="to give in; to die from something")
        newword.put();
        newword=ISEEVocabulary(id=51, wrd="eccentric", defn="unconventional; strange")
        newword.put();
        newword=ISEEVocabulary(id=52, wrd="obscure", defn="relatively unknown; not easily understood")
        newword.put();
        newword=ISEEVocabulary(id=53, wrd="extroverted", defn="interested in other people; the environment rather than oneself")
        newword.put();
        newword=ISEEVocabulary(id=54, wrd="sanctimonious", defn="ostentatiosly righteous; hypocritical; pretending to be holy")
        newword.put();
        newword=ISEEVocabulary(id=55, wrd="ecstatic", defn="joyful")
        newword.put();
        newword=ISEEVocabulary(id=56, wrd="rue", defn="to regret deeply")
        newword.put();
        newword=ISEEVocabulary(id=57, wrd="competent", defn="capable; fit")
        newword.put();
        newword=ISEEVocabulary(id=58, wrd="suffice", defn="to be enough")
        newword.put();
        newword=ISEEVocabulary(id=59, wrd="deject", defn="to dishearten; to depress")
        newword.put();
        newword=ISEEVocabulary(id=60, wrd="imminent", defn="about to happen; impending")
        newword.put();
        newword=ISEEVocabulary(id=61, wrd="devout", defn="very religious")
        newword.put();
        newword=ISEEVocabulary(id=62, wrd="vend", defn="to sell; offer for sale")
        newword.put();
        newword=ISEEVocabulary(id=63, wrd="reimburse", defn="to refund")
        newword.put();
        newword=ISEEVocabulary(id=64, wrd="emit", defn="to send out")
        newword.put();
        newword=ISEEVocabulary(id=65, wrd="persevere", defn="to continue despite challenges")
        newword.put();
        newword=ISEEVocabulary(id=66, wrd="scathing", defn="very severe; scornful")
        newword.put();
        newword=ISEEVocabulary(id=67, wrd="inhabit", defn="to live in")
        newword.put();
        newword=ISEEVocabulary(id=68, wrd="unkempt", defn="looking untidy or neglected")
        newword.put();
        newword=ISEEVocabulary(id=69, wrd="bind", defn="to tie or fasten")
        newword.put();
        newword=ISEEVocabulary(id=70, wrd="conform", defn="to obey; to follow rules")
        newword.put();
        newword=ISEEVocabulary(id=71, wrd="unanimous", defn="with everyone's agreement")
        newword.put();
        newword=ISEEVocabulary(id=72, wrd="condone", defn="to forgive; to overook")
        newword.put();
        newword=ISEEVocabulary(id=73, wrd="illiterate", defn="uneducated; not knowing how to read or write")
        newword.put();
        newword=ISEEVocabulary(id=74, wrd="placate", defn="to calm; to pacify")
        newword.put();
        newword=ISEEVocabulary(id=75, wrd="paradox", defn="contradiction; seemingly self-contradictory statement")
        newword.put();
        newword=ISEEVocabulary(id=76, wrd="conform", defn="to obey; to follow rules")
        newword.put();
        newword=ISEEVocabulary(id=77, wrd="congenial", defn="friendly; agreeable")
        newword.put();
        newword=ISEEVocabulary(id=78, wrd="corpulence", defn="fatness; obesity")
        newword.put();
        newword=ISEEVocabulary(id=79, wrd="splice", defn="to join by interweaving or overlapping the ends")
        newword.put();
        newword=ISEEVocabulary(id=80, wrd="pompous", defn="full of self-importance")
        newword.put();
        newword=ISEEVocabulary(id=81, wrd="obstruct", defn="to block; to hinder the movement or progress of")
        newword.put();
        newword=ISEEVocabulary(id=82, wrd="adjunct", defn="a non-essential supplement; something additional")
        newword.put();
        newword=ISEEVocabulary(id=83, wrd="rabble", defn="a disorderly crowd")
        newword.put();
        newword=ISEEVocabulary(id=84, wrd="tenacity", defn="persistence")
        newword.put();
        newword=ISEEVocabulary(id=85, wrd="plagiarism", defn="the act of passing off the ideas or writing of another as one's own")
        newword.put();
        newword=ISEEVocabulary(id=86, wrd="astute", defn="shrewd; observant; clever")
        newword.put();
        newword=ISEEVocabulary(id=87, wrd="recur", defn="to happen again or repeatedly")
        newword.put();
        newword=ISEEVocabulary(id=88, wrd="raze", defn="to destroy completely")
        newword.put();
        newword=ISEEVocabulary(id=89, wrd="adhere", defn="to stick to")
        newword.put();
        newword=ISEEVocabulary(id=90, wrd="compelling", defn="demanding of attention")
        newword.put();
        newword=ISEEVocabulary(id=91, wrd="lunge", defn="a sudden forward movement of the body; a thrust")
        newword.put();
        newword=ISEEVocabulary(id=92, wrd="fusion", defn="process of combining into one")
        newword.put();
        newword=ISEEVocabulary(id=93, wrd="diminish", defn="to make or become smaller in size")
        newword.put();
        newword=ISEEVocabulary(id=94, wrd="passive", defn="acted upon and not active; not resisting")
        newword.put();
        newword=ISEEVocabulary(id=95, wrd="debris", defn="bits and pieces of stone; rubbish")
        newword.put();
        newword=ISEEVocabulary(id=96, wrd="discerning", defn="able to see clearly")
        newword.put();
        newword=ISEEVocabulary(id=97, wrd="bounty", defn="generosity; a generous gift")
        newword.put();
        newword=ISEEVocabulary(id=98, wrd="devotee", defn="one strongly devoted to something")
        newword.put();
        newword=ISEEVocabulary(id=99, wrd="flagrant", defn="offensive; outrageous; deliberately shocking")
        newword.put();
        newword=ISEEVocabulary(id=100, wrd="insipid", defn="uninteresting; bland; dull")
        newword.put();
        newword=ISEEVocabulary(id=101, wrd="garrulous", defn="chatty; talkative")
        newword.put();
        newword=ISEEVocabulary(id=102, wrd="futile", defn="lacking purpose")
        newword.put();
        newword=ISEEVocabulary(id=103, wrd="dawdle", defn="to waste time; to loiter")
        newword.put();
        newword=ISEEVocabulary(id=104, wrd="schism", defn="division; split; discord")
        newword.put();
        newword=ISEEVocabulary(id=105, wrd="aggressive", defn="belligerent")
        newword.put();
        newword=ISEEVocabulary(id=106, wrd="misbegotten", defn="illegitimate; ill-conceived")
        newword.put();
        newword=ISEEVocabulary(id=107, wrd="glib", defn="articulate but insincere")
        newword.put();
        newword=ISEEVocabulary(id=108, wrd="germinate", defn="to begin to grow")
        newword.put();
        newword=ISEEVocabulary(id=109, wrd="divert", defn="to turn aside (from a course)")
        newword.put();
        newword=ISEEVocabulary(id=110, wrd="diplomatic", defn="of diplomacy; tactful")
        newword.put();
        newword=ISEEVocabulary(id=111, wrd="grovel", defn="to apologize profusely; to humble oneself")
        newword.put();
        newword=ISEEVocabulary(id=112, wrd="pedantic", defn="paying excessive attention to rules")
        newword.put();
        newword=ISEEVocabulary(id=113, wrd="gregarious", defn="sociable")
        newword.put();
        newword=ISEEVocabulary(id=114, wrd="grotesque", defn="distorted; fantastic; ridicuouls; absurd")
        newword.put();
        newword=ISEEVocabulary(id=115, wrd="bile", defn="the bitter, greenish fluid secreted by the liver")
        newword.put();
        newword=ISEEVocabulary(id=116, wrd="discursive", defn="rambling; getting off topic")
        newword.put();
        newword=ISEEVocabulary(id=117, wrd="dingy", defn="not clean or bright; grimy")
        newword.put();
        newword=ISEEVocabulary(id=118, wrd="fission", defn="process of breaking into parts")
        newword.put();
        newword=ISEEVocabulary(id=119, wrd="fidelity", defn="loyalty; faithful devotion")
        newword.put();
        newword=ISEEVocabulary(id=120, wrd="ransack", defn="to search thoroughly or roughly")
        newword.put();
        newword=ISEEVocabulary(id=121, wrd="fictitious", defn="untrue; false")
        newword.put();
        newword=ISEEVocabulary(id=122, wrd="fickle", defn="inconstant; not loyal")
        newword.put();
        newword=ISEEVocabulary(id=123, wrd="dogged", defn="subbornly persevering")
        newword.put();
        newword=ISEEVocabulary(id=124, wrd="doff", defn="to take off (one's hat)")
        newword.put();
        newword=ISEEVocabulary(id=125, wrd="demote", defn="to reduce to a lower rank")
        newword.put();
        newword=ISEEVocabulary(id=126, wrd="contend", defn="to compete; to struggle; to argue")
        newword.put();
        newword=ISEEVocabulary(id=127, wrd="ratify", defn="to approve formally; to confirm; to verify")
        newword.put();
        newword=ISEEVocabulary(id=128, wrd="recluse", defn="one who is shut off")
        newword.put();
        newword=ISEEVocabulary(id=129, wrd="hybrid", defn="an anumal or plant that is the offspring of two different species")
        newword.put();
        newword=ISEEVocabulary(id=130, wrd="piety", defn="holiness; religious devotion")
        newword.put();
        newword=ISEEVocabulary(id=131, wrd="boisterous", defn="cheerfully noisy or rough")
        newword.put();
        newword=ISEEVocabulary(id=132, wrd="harbinger", defn="something that foreshadows")
        newword.put();
        newword=ISEEVocabulary(id=133, wrd="ingenuous", defn="innocent; naive; guileless")
        newword.put();
        newword=ISEEVocabulary(id=134, wrd="suspense", defn="aanxious uncertainty while awaiting an event or an outcome")
        newword.put();
        newword=ISEEVocabulary(id=135, wrd="kinetic", defn="relating to motion")
        newword.put();
        newword=ISEEVocabulary(id=136, wrd="tepid", defn="lukewarm")
        newword.put();
        newword=ISEEVocabulary(id=137, wrd="intricate", defn="complicated or difficult")
        newword.put();
        newword=ISEEVocabulary(id=138, wrd="pugnacious", defn="combative; ready to fight")
        newword.put();
        newword=ISEEVocabulary(id=139, wrd="pungent", defn="strong or sharp smelling")
        newword.put();
        newword=ISEEVocabulary(id=140, wrd="warlock", defn="one that breaks faith; the devil; wizard")
        newword.put();
        newword=ISEEVocabulary(id=141, wrd="reek", defn="a strong unpleasant smell")
        newword.put();
        newword=ISEEVocabulary(id=142, wrd="barter", defn="to exchange good or property")
        newword.put();
        newword=ISEEVocabulary(id=143, wrd="disseminate", defn="to scatter or to spread")
        newword.put();
        newword=ISEEVocabulary(id=144, wrd="censor", defn="an official with the power to prohibit objectionable or obscene material")
        newword.put();
        newword=ISEEVocabulary(id=145, wrd="contemplate", defn="to gaze at or think about intently")
        newword.put();
        newword=ISEEVocabulary(id=146, wrd="tumult", defn="confusion; disorder; a loud, confused noise")
        newword.put();
        newword=ISEEVocabulary(id=147, wrd="usurp", defn="to seize another's power or rank")
        newword.put();
        newword=ISEEVocabulary(id=148, wrd="expunge", defn="to erase; to eliminate")
        newword.put();
        newword=ISEEVocabulary(id=149, wrd="oath", defn="a promise of truth")
        newword.put();
        newword=ISEEVocabulary(id=150, wrd="debilitate", defn="to weaken; to enfeeble")
        newword.put();
        newword=ISEEVocabulary(id=151, wrd="dearth", defn="scarcity; insufficiency")
        newword.put();
        newword=ISEEVocabulary(id=152, wrd="ebullient", defn="zestfully enthusiastic; boiling or seeming to boil")
        newword.put();
        newword=ISEEVocabulary(id=153, wrd="ostentatious", defn="showy; pretentious")
        newword.put();
        newword=ISEEVocabulary(id=154, wrd="verify", defn="to confirm the truth of something")
        newword.put();
        newword=ISEEVocabulary(id=155, wrd="reluctantly", defn="unwillingly")
        newword.put();
        newword=ISEEVocabulary(id=156, wrd="miniscule", defn="tiny; very small")
        newword.put();
        newword=ISEEVocabulary(id=157, wrd="mimicry", defn="imitation; aping")
        newword.put();
        newword=ISEEVocabulary(id=158, wrd="eddy", defn="a current of air or wind")
        newword.put();
        newword=ISEEVocabulary(id=159, wrd="conceal", defn="to hide; to keep secret")
        newword.put();
        newword=ISEEVocabulary(id=160, wrd="acclaim", defn="enthusiastic applause or approval")
        newword.put();
        newword=ISEEVocabulary(id=161, wrd="assess", defn="to judge; to determine amount or value")
        newword.put();
        newword=ISEEVocabulary(id=162, wrd="amateur", defn="non-professional; done for pleasure not pay; unskillful")
        newword.put();
        newword=ISEEVocabulary(id=163, wrd="critic", defn="one who judges")
        newword.put();
        newword=ISEEVocabulary(id=164, wrd="camouflage", defn="to disguise in order to conceal from the enemy")
        newword.put();
        newword=ISEEVocabulary(id=165, wrd="cache", defn="a place in which stores of food are hidden")
        newword.put();
        newword=ISEEVocabulary(id=166, wrd="amorphous", defn="having no determined form or shape")
        newword.put();
        newword=ISEEVocabulary(id=167, wrd="bizarre", defn="very odd or unusual")
        newword.put();
        newword=ISEEVocabulary(id=168, wrd="swift", defn="fast; quick")
        newword.put();
        newword=ISEEVocabulary(id=169, wrd="cantankerous", defn="bad-tempered; quarrelsome")
        newword.put();
        newword=ISEEVocabulary(id=170, wrd="humid", defn="damp; moist")
        newword.put();
        newword=ISEEVocabulary(id=171, wrd="etiquette", defn="acceptable manners in society")
        newword.put();
        newword=ISEEVocabulary(id=172, wrd="lagoon", defn="a salt-water lake by the sea")
        newword.put();
        newword=ISEEVocabulary(id=173, wrd="dogmatic", defn="opinionated; stubborn")
        newword.put();
        newword=ISEEVocabulary(id=174, wrd="dungeon", defn="dark underground cell")
        newword.put();
        newword=ISEEVocabulary(id=175, wrd="nourishment", defn="a source of strenght or support")
        newword.put();
        newword=ISEEVocabulary(id=176, wrd="ludicrous", defn="absurd; ridiculous")
        newword.put();
        newword=ISEEVocabulary(id=177, wrd="expansive", defn="broad and large")
        newword.put();
        newword=ISEEVocabulary(id=178, wrd="barrier", defn="an obstruction; anything that hinders or blocks")
        newword.put();
        newword=ISEEVocabulary(id=179, wrd="saucy", defn="impudent; mischievously or playfully provocative")
        newword.put();
        newword=ISEEVocabulary(id=180, wrd="lateral", defn="at the side")
        newword.put();
        newword=ISEEVocabulary(id=181, wrd="token", defn="something representing or expressing something else; on outward sign")
        newword.put();
        newword=ISEEVocabulary(id=182, wrd="effect", defn="something brought about by a cause or result")
        newword.put();
        newword=ISEEVocabulary(id=182, wrd="immaculate", defn="spotless; free from blemish; tidy")
        newword.put();
        newword=ISEEVocabulary(id=183, wrd="exhilarating", defn="exciting; full of high spirits")
        newword.put();
        newword=ISEEVocabulary(id=184, wrd="foundation", defn="establishment; basis")
        newword.put();
        newword=ISEEVocabulary(id=185, wrd="specify", defn="to identify precisely")
        newword.put();
        newword=ISEEVocabulary(id=186, wrd="satellite", defn="on object or body revolving around another")
        newword.put();
        newword=ISEEVocabulary(id=187, wrd="lunge", defn="a sudden forward movement of the body; a thrust")
        newword.put();
        newword=ISEEVocabulary(id=188, wrd="reveal", defn="to make known; to make visible by uncovering")
        newword.put();
        newword=ISEEVocabulary(id=189, wrd="adage", defn="wise, old saying")
        newword.put();
        newword=ISEEVocabulary(id=190, wrd="wretched", defn="very unhappy; contemptible")
        newword.put();
        newword=ISEEVocabulary(id=191, wrd="superb", defn="of the most impressive or splendid kind")
        newword.put();
        newword=ISEEVocabulary(id=192, wrd="abduct", defn="to kidnap")
        newword.put();
        newword=ISEEVocabulary(id=193, wrd="magnanimous", defn="unselfish")
        newword.put();
        newword=ISEEVocabulary(id=194, wrd="candor", defn="frankness; sincerity")
        newword.put();
        newword=ISEEVocabulary(id=195, wrd="egress", defn="exit")
        newword.put();
        newword=ISEEVocabulary(id=196, wrd="adept", defn="highly skilled; an expert")
        newword.put();
        newword=ISEEVocabulary(id=197, wrd="propel", defn="to push forwards or onwards")
        newword.put();
        newword=ISEEVocabulary(id=198, wrd="heed", defn="to pay attention to")
        newword.put();
        newword=ISEEVocabulary(id=199, wrd="regal", defn="like or fit for a king")
        newword.put();
        newword=ISEEVocabulary(id=200, wrd="malfunction", defn="faulty functioning")
        newword.put();
        newword=ISEEVocabulary(id=201, wrd="taciturn", defn="saying little; quiet")
        newword.put();
        newword=ISEEVocabulary(id=202, wrd="meager", defn="scanty in amount")
        newword.put();
        newword=ISEEVocabulary(id=203, wrd="barrage", defn="a curtain of artillery fire; any prolonged attack")
        newword.put();
        newword=ISEEVocabulary(id=204, wrd="altruism", defn="unselfishness; generosity")
        newword.put();
        newword=ISEEVocabulary(id=205, wrd="errant", defn="straying; mistaken")
        newword.put();
        newword=ISEEVocabulary(id=206, wrd="tamper", defn="to meddle or interfere with")
        newword.put();
        newword=ISEEVocabulary(id=207, wrd="olfactory", defn="concerned with the sense of smell")
        newword.put();
        newword=ISEEVocabulary(id=208, wrd="contiguous", defn="in contact; touching; near; next")
        newword.put();
        newword=ISEEVocabulary(id=209, wrd="lunge", defn="a sudden forward movement of the body; a thrust")
        newword.put();
        newword=ISEEVocabulary(id=210, wrd="tangible", defn="able to be perceived by touch; clear and definite; real")
        newword.put();
        newword=ISEEVocabulary(id=211, wrd="seethe", defn="bubble as if boiling; agitated or excited")
        newword.put();
        newword=ISEEVocabulary(id=212, wrd="vivacious", defn="lively")
        newword.put();
        newword=ISEEVocabulary(id=213, wrd="surmise", defn="to suppose; to conclude")
        newword.put();
        newword=ISEEVocabulary(id=214, wrd="flaw", defn="an imperfection")
        newword.put();
        newword=ISEEVocabulary(id=215, wrd="overwhelm", defn="to exhaust; to defeat")
        newword.put();
        newword=ISEEVocabulary(id=216, wrd="quench", defn="to satisfy (thirst); to extinguish (a fire)")
        newword.put();
        newword=ISEEVocabulary(id=217, wrd="obnoxious", defn="very unpleasant")
        newword.put();
        newword=ISEEVocabulary(id=218, wrd="option", defn="choice")
        newword.put();
        newword=ISEEVocabulary(id=219, wrd="collision", defn="a crash; a colliding")
        newword.put();
        newword=ISEEVocabulary(id=220, wrd="jubilee", defn="a special anniversary")
        newword.put();
        newword=ISEEVocabulary(id=221, wrd="savor", defn="flavor; smell; to enjoy fully")
        newword.put();
        newword=ISEEVocabulary(id=222, wrd="dexterous", defn="skilled in mind or body")
        newword.put();
        newword=ISEEVocabulary(id=223, wrd="expanse", defn="wide open area")
        newword.put();
        newword=ISEEVocabulary(id=224, wrd="saturate", defn="to make thoroughly wet; to fill or supply completely or to excess")
        newword.put();
        newword=ISEEVocabulary(id=225, wrd="animosity", defn="hatred; hostility")
        newword.put();
        newword=ISEEVocabulary(id=226, wrd="transplant", defn="to transfer")
        newword.put();
        newword=ISEEVocabulary(id=227, wrd="solitary", defn="living alone; without companions; lonely")
        newword.put();
        newword=ISEEVocabulary(id=228, wrd="earmark", defn="to set aside for special purpose; to identify")
        newword.put();
        newword=ISEEVocabulary(id=229, wrd="sentry", defn="a soldier posted to keep watch and guard something")
        newword.put();
        newword=ISEEVocabulary(id=230, wrd="bewildered", defn="to confuse hopelessly; to befuddle")
        newword.put();
        newword=ISEEVocabulary(id=231, wrd="brig", defn="a two-masted ship with square sails")
        newword.put();
        newword=ISEEVocabulary(id=232, wrd="quiver", defn="to shake or vibrate with a slight rapid motion")
        newword.put();
        newword=ISEEVocabulary(id=233, wrd="fauna", defn="the animals of a specifed time period")
        newword.put();
        newword=ISEEVocabulary(id=234, wrd="observation", defn="watching carefully; noticing things")
        newword.put();
        newword=ISEEVocabulary(id=235, wrd="advantageous", defn="profitable; helpful")
        newword.put();
        newword=ISEEVocabulary(id=236, wrd="elusive", defn="hard to capture or understand")
        newword.put();
        newword=ISEEVocabulary(id=237, wrd="ensnare", defn="to catch in a trap")
        newword.put();
        newword=ISEEVocabulary(id=238, wrd="limber", defn="supple; agile; flexible")
        newword.put();
        newword=ISEEVocabulary(id=239, wrd="canine", defn="of or like a dog")
        newword.put();
        newword=ISEEVocabulary(id=240, wrd="skit", defn="a brief dramatic sketch")
        newword.put();
        newword=ISEEVocabulary(id=241, wrd="significant", defn="having meaning; having importance")
        newword.put();
        newword=ISEEVocabulary(id=242, wrd="stress", defn="pressure; mental or emotional strain")
        newword.put();
        newword=ISEEVocabulary(id=243, wrd="random", defn="done or occurring without method")
        newword.put();
        newword=ISEEVocabulary(id=244, wrd="disclaim", defn="to give up any claim; to repudiate")
        newword.put();
        newword=ISEEVocabulary(id=245, wrd="erudite", defn="learned; scholarly")
        newword.put();
        newword=ISEEVocabulary(id=246, wrd="encompass", defn="to surround; to contain")
        newword.put();
        newword=ISEEVocabulary(id=247, wrd="rendezvous", defn="a pre-arranged meeting or meeting place")
        newword.put();
        newword=ISEEVocabulary(id=248, wrd="sustain", defn="to support; to maintain")
        newword.put();
        newword=ISEEVocabulary(id=249, wrd="artifice", defn="skill or ingenuity")
        newword.put();
        newword=ISEEVocabulary(id=250, wrd="evacuate", defn="to leave empty; to withdraw")
        newword.put();
        newword=ISEEVocabulary(id=251, wrd="tether", defn="a rope or chain for tying an animal down")
        newword.put();
        newword=ISEEVocabulary(id=252, wrd="chronic", defn="lasting a long time")
        newword.put();
        newword=ISEEVocabulary(id=253, wrd="indicate", defn="to point out")
        newword.put();
        newword=ISEEVocabulary(id=254, wrd="copious", defn="plentiful; large in quantity")
        newword.put();
        newword=ISEEVocabulary(id=255, wrd="era", defn="a period of time/history (with a special characteristic)")
        newword.put();
        newword=ISEEVocabulary(id=256, wrd="ignite", defn="to set fire; to catch fire")
        newword.put();
        newword=ISEEVocabulary(id=257, wrd="discord", defn="conflict; argument")
        newword.put();
        newword=ISEEVocabulary(id=258, wrd="jeer", defn="laugh or shout rudely or scornfully")
        newword.put();
        newword=ISEEVocabulary(id=259, wrd="marvel", defn="a wonderful thing; to feel wonder")
        newword.put();
        newword=ISEEVocabulary(id=260, wrd="grave", defn="serious")
        newword.put();
        newword=ISEEVocabulary(id=261, wrd="fund", defn="to supply; to offer money or support")
        newword.put();
        newword=ISEEVocabulary(id=262, wrd="harsh", defn="unpleasant; offensive; cruel; severe")
        newword.put();
        newword=ISEEVocabulary(id=263, wrd="allege", defn="to declare without proof")
        newword.put();
        newword=ISEEVocabulary(id=264, wrd="hasten", defn="to speed up; to hurry")
        newword.put();                       
        newword=ISEEVocabulary(id=265, wrd="melancholy", defn="sadness; state of grief")
        newword.put();                       
        newword=ISEEVocabulary(id=266, wrd="flow", defn="to move like a liquid; to pour out")
        newword.put();
        newword=ISEEVocabulary(id=267, wrd="orbit", defn="a path described by one body in its revolution around another")
        newword.put();                       
        newword=ISEEVocabulary(id=268, wrd="vehement", defn="showing strong feeling")
        newword.put();
        newword=ISEEVocabulary(id=269, wrd="vex", defn="to annoy; to irritate")
        newword.put();
        newword=ISEEVocabulary(id=270, wrd="sociable", defn="fond of company; characterized by friendly companionship")
        newword.put();
        newword=ISEEVocabulary(id=271, wrd="timid", defn="shy; scared; fearful")
        newword.put();
        newword=ISEEVocabulary(id=272, wrd="tamper", defn="to meddle or interfere with")
        newword.put();
        newword=ISEEVocabulary(id=273, wrd="surrogate", defn="a substitute")
        newword.put();
        newword=ISEEVocabulary(id=274, wrd="taint", defn="to spoil; to contaminate")
        newword.put();
        newword=ISEEVocabulary(id=275, wrd="trite", defn="hackneyed; overused")
        newword.put();
        newword=ISEEVocabulary(id=276, wrd="trickle", defn="to flow slowly; to move little by little")
        newword.put();
        newword=ISEEVocabulary(id=277, wrd="meek", defn="quiet and obedient; not protesting")
        newword.put();
        newword=ISEEVocabulary(id=278, wrd="tactful", defn="a keen sense of keeping good relations and avoiding offense")
        newword.put();
        newword=ISEEVocabulary(id=279, wrd="mar", defn="to disfigure; to spoil")
        newword.put();
        newword=ISEEVocabulary(id=280, wrd="malleable", defn="easily changed")
        newword.put();
        newword=ISEEVocabulary(id=281, wrd="insolent", defn="offensive; insulting")
        newword.put();
        newword=ISEEVocabulary(id=282, wrd="ingenious", defn="original; creative")
        newword.put();
        newword=ISEEVocabulary(id=283, wrd="adjourn", defn="to suspend (a meeting) for a period of time")
        newword.put();
        newword=ISEEVocabulary(id=284, wrd="quell", defn="to quiet; to suppress")
        newword.put();
        newword=ISEEVocabulary(id=285, wrd="behold", defn="to look at; to observe")
        newword.put();
        newword=ISEEVocabulary(id=286, wrd="conserve", defn="to save; prevent wastage")
        newword.put();
        newword=ISEEVocabulary(id=287, wrd="congregate", defn="to gather together")
        newword.put();
        newword=ISEEVocabulary(id=288, wrd="surfeit", defn="an excessive number; an overindulgence")
        newword.put();
        newword=ISEEVocabulary(id=289, wrd="glee", defn="lively joy")
        newword.put();
        newword=ISEEVocabulary(id=290, wrd="notify", defn="to inform")
        newword.put();
        newword=ISEEVocabulary(id=291, wrd="scarcely", defn="hardly; barely")
        newword.put();
        newword=ISEEVocabulary(id=292, wrd="vandalism", defn="intentional destruction of work or private property")
        newword.put();
        newword=ISEEVocabulary(id=293, wrd="reinforce", defn="to strengthen with additional forces")
        newword.put();
        newword=ISEEVocabulary(id=294, wrd="cajole", defn="to persuade; to coax")
        newword.put();
        newword=ISEEVocabulary(id=295, wrd="coalesce", defn="to come together; to unite")
        newword.put();
        newword=ISEEVocabulary(id=296, wrd="apt", defn="likely; relevant")
        newword.put();
        newword=ISEEVocabulary(id=297, wrd="tolerate", defn="to deal with; permit")
        newword.put();
        newword=ISEEVocabulary(id=298, wrd="compassion", defn="deep sympathy; pity")
        newword.put();
        newword=ISEEVocabulary(id=299, wrd="botanist", defn="one who studies plant life")
        newword.put();
        newword=ISEEVocabulary(id=300, wrd="pursue", defn="to follow; to try to catch or attack")
        newword.put();
        newword=ISEEVocabulary(id=301, wrd="refrain", defn="to hold back; to suppress")
        newword.put();
        newword=ISEEVocabulary(id=302, wrd="variegated", defn="multi-colored")
        newword.put();
        newword=ISEEVocabulary(id=303, wrd="audacious", defn="bold; daring; fearless")
        newword.put();
        newword=ISEEVocabulary(id=304, wrd="ascertain", defn="to find out with certainty")
        newword.put();
        newword=ISEEVocabulary(id=305, wrd="erode", defn="to wear away")
        newword.put();
        newword=ISEEVocabulary(id=306, wrd="extricate", defn="to free")
        newword.put();
        newword=ISEEVocabulary(id=307, wrd="epoch", defn="a period of time in history")
        newword.put();
        newword=ISEEVocabulary(id=308, wrd="extraction", defn="the process of taking out by effort; origin or descent")
        newword.put();
        newword=ISEEVocabulary(id=309, wrd="exotic", defn="foreign; strangely beautiful")
        newword.put();
        newword=ISEEVocabulary(id=310, wrd="meteorologist", defn="someone who forecasts the weather")
        newword.put();
        newword=ISEEVocabulary(id=311, wrd="nauseous", defn="causing nausea or disgust")
        newword.put();
        newword=ISEEVocabulary(id=312, wrd="mourn", defn="to feel or express sorrow")
        newword.put();
        newword=ISEEVocabulary(id=313, wrd="ravenous", defn="extremely hungry")
        newword.put();
        newword=ISEEVocabulary(id=314, wrd="obstacle", defn="a hindrance")
        newword.put();
        newword=ISEEVocabulary(id=315, wrd="nebulous", defn="vague; cloudy")
        newword.put();
        newword=ISEEVocabulary(id=316, wrd="mutation", defn="a change; alteration in the genes")
        newword.put();
        newword=ISEEVocabulary(id=317, wrd="murky", defn="dark; gloomy")
        newword.put();
        newword=ISEEVocabulary(id=318, wrd="vacuous", defn="empty; void; lacking intelligence")
        newword.put();
        newword=ISEEVocabulary(id=319, wrd="nomadic", defn="moving from place to place")
        newword.put();
        newword=ISEEVocabulary(id=320, wrd="nimble", defn="able to move quickly")
        newword.put();
        newword=ISEEVocabulary(id=321, wrd="countenance", defn="to favor; to support; a person's face")
        newword.put();
        newword=ISEEVocabulary(id=322, wrd="alleviate", defn="to reveal; to ease pain")
        newword.put();
        newword=ISEEVocabulary(id=323, wrd="aperture", defn="an opening; hole")
        newword.put();
        newword=ISEEVocabulary(id=324, wrd="akin", defn="related; similar")
        newword.put();
        newword=ISEEVocabulary(id=325, wrd="benevolent", defn="generous; charitable; well-meaning")
        newword.put();
        newword=ISEEVocabulary(id=326, wrd="infectious", defn="likely to spread or cause an infection")
        newword.put();
        newword=ISEEVocabulary(id=327, wrd="adversary", defn="an enemy; opponent; foe")
        newword.put();
        newword=ISEEVocabulary(id=328, wrd="temperate", defn="without extremes; self-restrained")
        newword.put();
        newword=ISEEVocabulary(id=329, wrd="aghast", defn="feeling great honor or dismamy")
        newword.put();
        newword=ISEEVocabulary(id=330, wrd="atrocious", defn="very wicked; very bad")
        newword.put();
        newword=ISEEVocabulary(id=331, wrd="aspire", defn="to hope; to have ambition")
        newword.put();
        newword=ISEEVocabulary(id=332, wrd="abdicate", defn="to give up power of position")
        newword.put();
        newword=ISEEVocabulary(id=333, wrd="declaim", defn="to speak in a dramatic way")
        newword.put();
        newword=ISEEVocabulary(id=334, wrd="amend", defn="to change; to alter slightly")
        newword.put();
        newword=ISEEVocabulary(id=335, wrd="allure", defn="to entice; to attract")
        newword.put();
        newword=ISEEVocabulary(id=336, wrd="cascade", defn="a small steep waterfall")
        newword.put();
        newword=ISEEVocabulary(id=337, wrd="affectation", defn="a pretending to like; artificial behavior")
        newword.put();
        newword=ISEEVocabulary(id=338, wrd="articulate", defn="able to express oneself coherently")
        newword.put();
        newword=ISEEVocabulary(id=339, wrd="curvature", defn="a curving; being curved")
        newword.put();
        newword=ISEEVocabulary(id=340, wrd="accelerate", defn="to increase in speed")
        newword.put();
        newword=ISEEVocabulary(id=341, wrd="circulate", defn="to pass around; move from place to place")
        newword.put();
        newword=ISEEVocabulary(id=342, wrd="absurd", defn="tunreasonable; ridiculous")
        newword.put();
        newword=ISEEVocabulary(id=343, wrd="confidential", defn="secret")
        newword.put();
        newword=ISEEVocabulary(id=344, wrd="coupled", defn="two successive rhyming lines of poetry")
        newword.put();
        newword=ISEEVocabulary(id=345, wrd="flounder", defn="to stumble; fall; sink")
        newword.put();
        newword=ISEEVocabulary(id=346, wrd="flippant", defn="disrespectful; frivolous; saucy")
        newword.put();
        newword=ISEEVocabulary(id=347, wrd="disputatious", defn="fond of arguing")
        newword.put();
        newword=ISEEVocabulary(id=348, wrd="formidable", defn="awesome; difficult to achieve")
        newword.put();
        newword=ISEEVocabulary(id=349, wrd="dismal", defn="causing gloom or misery")
        newword.put();
        newword=ISEEVocabulary(id=350, wrd="rabid", defn="furious; fanatical")
        newword.put();
        newword=ISEEVocabulary(id=351, wrd="tamper", defn="to meddle or interfere with")
        newword.put();
        newword=ISEEVocabulary(id=352, wrd="amphibian", defn="animal or plant living both on land and in water")
        newword.put();
        newword=ISEEVocabulary(id=353, wrd="assail", defn="to attack violently")
        newword.put();
        newword=ISEEVocabulary(id=354, wrd="amorous", defn="expressing love")
        newword.put();
        newword=ISEEVocabulary(id=355, wrd="choreographer", defn="one who devises dances or ballets")
        newword.put();
        newword=ISEEVocabulary(id=356, wrd="annihilate", defn="to destroy violently")
        newword.put();
        newword=ISEEVocabulary(id=357, wrd="sequel", defn="what follows, especially as a result")
        newword.put();
        newword=ISEEVocabulary(id=358, wrd="catastrophe", defn="sudden, great disaster")
        newword.put();
        newword=ISEEVocabulary(id=359, wrd="aimless", defn="having no purpose")
        newword.put();
        newword=ISEEVocabulary(id=360, wrd="stealthy", defn="quiet and cautious")
        newword.put();
        newword=ISEEVocabulary(id=361, wrd="tamper", defn="to meddle or interfere with")
        newword.put();
        newword=ISEEVocabulary(id=362, wrd="squander", defn="to waste")
        newword.put();
        newword=ISEEVocabulary(id=363, wrd="squalid", defn="dirty, unpleasant")
        newword.put();
        newword=ISEEVocabulary(id=364, wrd="foretell", defn="to predict")
        newword.put();
        newword=ISEEVocabulary(id=365, wrd="eminent", defn="towering or standing out above")
        newword.put();
        newword=ISEEVocabulary(id=366, wrd="taut", defn="stretched tightly")
        newword.put();
        newword=ISEEVocabulary(id=367, wrd="residue", defn="what is left over")
        newword.put();
        newword=ISEEVocabulary(id=368, wrd="sheer", defn="complete or absolute")
        newword.put();
        newword=ISEEVocabulary(id=369, wrd="rancorous", defn="having deep-seated ill-will")
        newword.put();
        newword=ISEEVocabulary(id=370, wrd="ominous", defn="threatening; menacing")
        newword.put();
        newword=ISEEVocabulary(id=371, wrd="subdue", defn="to restrain; hold back")
        newword.put();
        newword=ISEEVocabulary(id=372, wrd="suave", defn="charming; confident; elegant")
        newword.put();
        newword=ISEEVocabulary(id=373, wrd="opportune", defn="favorable; well-timed")
        newword.put();
        newword=ISEEVocabulary(id=374, wrd="insomnia", defn="inability to sleep")
        newword.put();
        newword=ISEEVocabulary(id=375, wrd="insurgency", defn="an uprising; a rebellion")
        newword.put();
        newword=ISEEVocabulary(id=376, wrd="intangible", defn="incapable of being touched")
        newword.put();
        newword=ISEEVocabulary(id=377, wrd="ironic", defn="contradictory; inconsistent; sarcastic")
        newword.put();
        newword=ISEEVocabulary(id=378, wrd="inundated", defn="flooded")
        newword.put();
        newword=ISEEVocabulary(id=379, wrd="irate", defn="angry")
        newword.put();
        newword=ISEEVocabulary(id=380, wrd="itinerant", defn="traveling")
        newword.put();
        newword=ISEEVocabulary(id=381, wrd="indict", defn="to make a formal accusation against")
        newword.put();
        newword=ISEEVocabulary(id=382, wrd="inert", defn="without power to move")
        newword.put();
        newword=ISEEVocabulary(id=383, wrd="skeptical", defn="incredulous")
        newword.put();
        newword=ISEEVocabulary(id=384, wrd="incentive", defn="a motive; stimulus")
        newword.put();
        newword=ISEEVocabulary(id=385, wrd="impious", defn="disrespectful (especially of god)")
        newword.put();
        newword=ISEEVocabulary(id=386, wrd="inadvertent", defn="not paying attention; not observant")
        newword.put();
        newword=ISEEVocabulary(id=387, wrd="imperceptible", defn="un-noticeable; slight")
        newword.put();
        newword=ISEEVocabulary(id=388, wrd="impervious", defn="unable to be penetrated or influenced")
        newword.put();
        newword=ISEEVocabulary(id=389, wrd="lethargic", defn="sluggish; weak")
        newword.put();
        newword=ISEEVocabulary(id=390, wrd="spurn", defn="to reject; to scorn")
        newword.put();
        newword=ISEEVocabulary(id=391, wrd="aqueous", defn="of, like or formed by water")
        newword.put();
        newword=ISEEVocabulary(id=392, wrd="adorn", defn="to decorate")
        newword.put();
        newword=ISEEVocabulary(id=393, wrd="acute", defn="very sharp; severe")
        newword.put();
        newword=ISEEVocabulary(id=394, wrd="angular", defn="with sharp angles")
        newword.put();
        newword=ISEEVocabulary(id=395, wrd="abyss", defn="bottomless gulf")
        newword.put();
        newword=ISEEVocabulary(id=396, wrd="anxiety", defn="state of fear andn uncertainty")
        newword.put();
        newword=ISEEVocabulary(id=397, wrd="conventional", defn="traditional")
        newword.put();
        newword=ISEEVocabulary(id=398, wrd="arid", defn="extremely dry")
        newword.put();
        newword=ISEEVocabulary(id=399, wrd="choleric", defn="easily angered")
        newword.put();
        newword=ISEEVocabulary(id=400, wrd="abhor", defn="to hate; to detest")
        newword.put();
        newword=ISEEVocabulary(id=401, wrd="courier", defn="a messenger")
        newword.put();
        newword=ISEEVocabulary(id=401, wrd="counsel", defn="advise")
        newword.put();
        newword=ISEEVocabulary(id=402, wrd="concise", defn="condensed; brief")
        newword.put();
        newword=ISEEVocabulary(id=403, wrd="authoritative", defn="having authority; commanding")
        newword.put();
        newword=ISEEVocabulary(id=404, wrd="affable", defn="friendly; easy-going")
        newword.put();
        newword=ISEEVocabulary(id=405, wrd="constrict", defn="to make narrower by squeezing")
        newword.put();
        newword=ISEEVocabulary(id=406, wrd="agitate", defn="to stir or shake-up")
        newword.put();
        newword=ISEEVocabulary(id=407, wrd="glistening", defn="shining brightly")
        newword.put();
        newword=ISEEVocabulary(id=408, wrd="poll", defn="a survey of public opinion")
        newword.put();
        newword=ISEEVocabulary(id=409, wrd="reign", defn="a king's period of rule")
        newword.put();
        newword=ISEEVocabulary(id=410, wrd="entice", defn="to tempt")
        newword.put();
        newword=ISEEVocabulary(id=411, wrd="cue", defn="a signal; hint")
        newword.put();
        newword=ISEEVocabulary(id=412, wrd="suppress", defn="to put an end to")
        newword.put();
        newword=ISEEVocabulary(id=413, wrd="susceptible", defn="easily affected or influenced")
        newword.put();
        newword=ISEEVocabulary(id=414, wrd="procrastinate", defn="to postpone action")
        newword.put();
        newword=ISEEVocabulary(id=415, wrd="prevail", defn="to gain victory")
        newword.put();
        newword=ISEEVocabulary(id=416, wrd="prophesy", defn="prediction of future events")
        newword.put();
        newword=ISEEVocabulary(id=417, wrd="slack", defn="not tight")
        newword.put();
        newword=ISEEVocabulary(id=418, wrd="unaccustomed", defn="not used to something")
        newword.put();
        newword=ISEEVocabulary(id=419, wrd="nullify", defn="to cancel; to invalidate")
        newword.put();
        newword=ISEEVocabulary(id=420, wrd="tamper", defn="to meddle or interfere with")
        newword.put();
        newword=ISEEVocabulary(id=421, wrd="profound", defn="deep")
        newword.put();
        newword=ISEEVocabulary(id=422, wrd="astound", defn="to astonish greatly")
        newword.put();
        newword=ISEEVocabulary(id=423, wrd="communicative", defn="giving or exchanging information or messages")
        newword.put();
        newword=ISEEVocabulary(id=424, wrd="aloof", defn="detached; indifferent; distant")
        newword.put();
        newword=ISEEVocabulary(id=425, wrd="aforementioned", defn="said or mentioned before")
        newword.put();
        newword=ISEEVocabulary(id=426, wrd="arouse", defn="to awaken")
        newword.put();
        newword=ISEEVocabulary(id=427, wrd="bliss", defn="great happiness; spiritual joy")
        newword.put();
        newword=ISEEVocabulary(id=428, wrd="decade", defn="period of 10 years")
        newword.put();
        newword=ISEEVocabulary(id=429, wrd="innocent", defn="not guilty; free of sin")
        newword.put();
        newword=ISEEVocabulary(id=430, wrd="decay", defn="to spoil or go bad")
        newword.put();
        newword=ISEEVocabulary(id=431, wrd="hallowed", defn="holy or sacred")
        newword.put();
        newword=ISEEVocabulary(id=432, wrd="benefactor", defn="a donor")
        newword.put();
        newword=ISEEVocabulary(id=433, wrd="phenomenon", defn="something unusual")
        newword.put();
        newword=ISEEVocabulary(id=434, wrd="beneficial", defn="helpful")
        newword.put();
        newword=ISEEVocabulary(id=435, wrd="brash", defn="insolent; impudent")
        newword.put();
        newword=ISEEVocabulary(id=436, wrd="recalcitrant", defn="obstinately disobedient")
        newword.put();
        newword=ISEEVocabulary(id=437, wrd="succeed", defn="to achieve one's aims or goals")
        newword.put();
        newword=ISEEVocabulary(id=438, wrd="ultimate", defn="final; extreme")
        newword.put();
        newword=ISEEVocabulary(id=439, wrd="ferocious", defn="fierce; savage")
        newword.put();
        newword=ISEEVocabulary(id=440, wrd="doze", defn="to nap")
        newword.put();
        newword=ISEEVocabulary(id=441, wrd="finale", defn="the ending")
        newword.put();
        newword=ISEEVocabulary(id=442, wrd="fragile", defn="easily broken; delicate")
        newword.put();
        newword=ISEEVocabulary(id=443, wrd="frequent", defn="happening often")
        newword.put();
        newword=ISEEVocabulary(id=444, wrd="herbivorous", defn="feeding mainly on plants and grass")
        newword.put();
        newword=ISEEVocabulary(id=445, wrd="hexagon", defn="plane figure with six angles and six sides")
        newword.put();
        newword=ISEEVocabulary(id=446, wrd="horrid", defn="causing horror; very bad; ugly")
        newword.put();
        newword=ISEEVocabulary(id=447, wrd="hive", defn="shelter for a colony of bees")
        newword.put();
        newword=ISEEVocabulary(id=448, wrd="hibernate", defn="to spend the winter sleeping")
        newword.put();
        newword=ISEEVocabulary(id=449, wrd="hatch", defn="to break out of a egg; to produce a plan")
        newword.put();
        newword=ISEEVocabulary(id=450, wrd="pedestrian", defn="a person walking; commonplace or dull")
        newword.put();
        newword=ISEEVocabulary(id=451, wrd="terminate", defn="to come or bring to an end")
        newword.put();
        newword=ISEEVocabulary(id=452, wrd="terse", defn="concise; abrupt; pithy")
        newword.put();
        newword=ISEEVocabulary(id=453, wrd="orchid", defn="a showy flower")
        newword.put();
        newword=ISEEVocabulary(id=454, wrd="vivid", defn="intense; clear")
        newword.put();
        newword=ISEEVocabulary(id=455, wrd="vacate", defn="cease to occupy")
        newword.put();
        newword=ISEEVocabulary(id=456, wrd="implicit", defn="understood without being directly expressed")
        newword.put();
        newword=ISEEVocabulary(id=457, wrd="staunch", defn="unshakeably loyal")
        newword.put();
        newword=ISEEVocabulary(id=458, wrd="shrewd", defn="clever; astute")
        newword.put();
        newword=ISEEVocabulary(id=459, wrd="enact", defn="to pass a law; to represent in a play")
        newword.put();
        newword=ISEEVocabulary(id=460, wrd="vague", defn="not clearly explained")
        newword.put();
        newword=ISEEVocabulary(id=461, wrd="agility", defn="quickness and ease of movement")
        newword.put();
        newword=ISEEVocabulary(id=462, wrd="biased", defn="prejudiced; influenced")
        newword.put();
        newword=ISEEVocabulary(id=463, wrd="despicable", defn="deserving scorn; contemptible")
        newword.put();
        newword=ISEEVocabulary(id=464, wrd="desolate", defn="lifeless; empty")
        newword.put();
        newword=ISEEVocabulary(id=465, wrd="wanton", defn="irresponsible")
        newword.put();
        newword=ISEEVocabulary(id=466, wrd="wan", defn="sickly pale")
        newword.put();
        newword=ISEEVocabulary(id=467, wrd="vitality", defn="energy; power to survive")
        newword.put();
        newword=ISEEVocabulary(id=468, wrd="tyranny", defn="cruel exercise of power")
        newword.put();
        newword=ISEEVocabulary(id=469, wrd="scrupulous", defn="honest; careful")
        newword.put();
        newword=ISEEVocabulary(id=470, wrd="sinister", defn="suggesting something evil is at hand")
        newword.put();
        newword=ISEEVocabulary(id=471, wrd="procure", defn="to obtain by care or effort")
        newword.put();
        newword=ISEEVocabulary(id=472, wrd="admonish", defn="to reprove or warn")
        newword.put();
        newword=ISEEVocabulary(id=473, wrd="solicit", defn="to ask for something")
        newword.put();
        newword=ISEEVocabulary(id=474, wrd="repudiate", defn="to reject; cancel")
        newword.put();
        newword=ISEEVocabulary(id=475, wrd="renowned", defn="famous")
        newword.put();
        newword=ISEEVocabulary(id=476, wrd="revelry", defn="lively festivity")
        newword.put();
        newword=ISEEVocabulary(id=477, wrd="mandatory", defn="necessary; required")
        newword.put();
        newword=ISEEVocabulary(id=478, wrd="deadlock", defn="a standstill resulting from equal and opposed forces")
        newword.put();
        newword=ISEEVocabulary(id=479, wrd="burnish", defn="to polish")
        newword.put();
        newword=ISEEVocabulary(id=480, wrd="banal", defn="commonplace")
        newword.put();
        newword=ISEEVocabulary(id=481, wrd="petrify", defn="to become stone")
        newword.put();
        newword=ISEEVocabulary(id=482, wrd="candid", defn="honest; truthful")
        newword.put();
        newword=ISEEVocabulary(id=483, wrd="hovel", defn="small hut")
        newword.put();
        newword=ISEEVocabulary(id=484, wrd="repartee", defn="an exchange of witty remarks")
        newword.put();
        newword=ISEEVocabulary(id=485, wrd="gruesome", defn="causing horrow; grisly")
        newword.put();
        newword=ISEEVocabulary(id=486, wrd="embellish", defn="to adorn; to add details")
        newword.put();
        newword=ISEEVocabulary(id=487, wrd="immortal", defn="living forever")
        newword.put();
        newword=ISEEVocabulary(id=488, wrd="fanatic", defn="overly enthusiastic person")
        newword.put();
        newword=ISEEVocabulary(id=489, wrd="fatal", defn="deadly")
        newword.put();
        newword=ISEEVocabulary(id=490, wrd="banish", defn="to exile")
        newword.put();
        newword=ISEEVocabulary(id=491, wrd="circumscribe", defn="to draw a line around")
        newword.put();
        newword=ISEEVocabulary(id=492, wrd="secure", defn="tightly fixed")
        newword.put();
        newword=ISEEVocabulary(id=493, wrd="summit", defn="top of a mountain")
        newword.put();
        newword=ISEEVocabulary(id=494, wrd="enigma", defn="puzzle; mystery")
        newword.put();
        newword=ISEEVocabulary(id=495, wrd="scald", defn="to injure with hot liquid or steam")
        newword.put();
        newword=ISEEVocabulary(id=496, wrd="trace", defn="a small amount")
        newword.put();
        newword=ISEEVocabulary(id=497, wrd="obtuse", defn="slow to understand")
        newword.put();
        newword=ISEEVocabulary(id=498, wrd="chasm", defn="any break or gap")
        newword.put();
        newword=ISEEVocabulary(id=499, wrd="antidote", defn="substance that counteracts effect of poison")
        newword.put();
        newword=ISEEVocabulary(id=500, wrd="classify", defn="to organize")
        newword.put();
        newword=ISEEVocabulary(id=501, wrd="aroma", defn="pleasant odor")
        newword.put();
        newword=ISEEVocabulary(id=502, wrd="celestial", defn="heavenly")
        newword.put();
        
    
                   
    def post(self):
        words=self.init_words() 

class RepeatPage(webapp.RequestHandler):

    def get(self):

        randid=random.randrange(1,502)
        resultset = db.GqlQuery("SELECT * FROM ISEEVocabulary")
       
        template_values = {
            'word':resultset[randid]
            }

        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/more', RepeatPage),
                                      ('/queue', QueuePage),
                                      ])

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
