# -*- coding: utf-8 -*-
from Demos.SendSimpleEmail.SendSimpleEmail import send_mail
import json
import time

mail_server = "smtp-mail.outlook.com"


# outlook change

def readConfig():
    with open('mailUsers.json') as data_file:
        return json.load(data_file)


def generateContent():
    return '''
    In a statement released Sunday evening, Clinton campaign manager Robby Mook said, "On the eve of what the Trump campaign has billed as a major foreign policy speech, we have learned of more troubling connections between Donald Trump's team and pro-Kremlin elements in Ukraine."
    He continued, "Given the pro-Putin policy stances adopted by Donald Trump and the recent Russian government hacking and disclosure of Democratic Party records, Donald Trump has a responsibility to disclose campaign chair Paul Manafort's and all other campaign employees' and advisers' ties to Russian or pro-Kremlin entities, including whether any of Trump's employees or advisers are currently representing and or being paid by them."
    Mook's response came in after the Times report about the discovery by anti-corruption investigators of "$12.7 million in undisclosed cash payments designated for Mr. Manafort from [then-President of Ukraine Viktor Yanukovich's] pro-Russian political party from 2007 to 2012, according to Ukraine's newly formed National Anti-Corruption Bureau."
    According to the report, anti-corruption officials and investigators in Ukraine argue that the payments they discovered are part of a large, secret network of corruption operated by the government under Yanukovich, for whom Manafort worked as a consultant at the time.
    The report also noted that those officials have not yet determined if Manafort received the payments found in the handwritten ledgers. Manafort's lawyer, Richard Hibey, denied to the Times that his client received "any such cash payments" described in the report.
    Manafort called the report "unfounded, silly, and nonsensical."
    "Once again The New York Times has chosen to purposefully ignore facts and professional journalism to fit their political agenda, choosing to attack my character and reputation rather than present an honest report," he said in a statement.
    "The simplest answer is the truth: I am a campaign professional. It is well known that I do work in the United States and have done work on overseas campaigns as well. I have never received a single "off-the-books cash payment" as falsely "reported" by The New York Times, nor have I ever done work for the governments of Ukraine or Russia. Further, all of the political payments directed to me were for my entire political team: campaign staff (local and international), polling and research, election integrity and television advertising. The suggestion that I accepted cash payments is unfounded, silly, and nonsensical.
    "My work in Ukraine ceased following the country's parliamentary elections in October 2014. In addition, as the article points out hesitantly, every government official interviewed states I have done nothing wrong, and there is no evidence of 'cash payments' made to me by any official in Ukraine. However, the Times does fail to disclose the fact that the Clinton Foundation has taken (and may still take) payments in exchange for favors from Hillary Clinton while serving as the Secretary of State. This is not discussed despite the overwhelming evidence in emails that Hillary Clinton attempted to cover up," the statement continued.
    Prior to serving as chairman of the Trump campaign, Manafort previously worked on and off as a political consultant for Yanukovich, before Yanukovich's violent ouster in 2014.
    Corey Lewandowski, who served as Trump's campaign manager before Manafort took over as chairman in a reportedly contentious transfer of power, tweeted out a link to the Times report late Sunday, and addressed the controversial story on "New Day" on CNN Monday.
    Asked why he shared the story, and if it was an attempt to criticize Manafort, Lewandowski answered instead that the report was an example of anti-Trump bias in the media.
    "The media is now focusing on a private person who had a private business model, which no one says there's anything illegal about what he did," he said on CNN.
    "Number one, Paul says there was no money received. Number two, there's no proof of any money received. Number three, Cheryl Mills was a government employee at the time," Lewandowski added, comparing the scrutiny of Manafort to criticism of Clinton aide Cheryl Mills and the overlap between her duties as a State Dept. official under Clinton and her work with the Clinton Foundation.
    RELATED: Clinton aide Cheryl Mills aided Clinton Foundation
    Manafort's work there has come under scrutiny and drawn flak for the Trump campaign, particularly as the standoff between Ukraine and Russia devolved into violence following Yanukovich's flight to Russia, and as the Yanukovich government's pro-Russian ties and corruption have been made public in reports such as that in the Times. That scrutiny has increased in response to the suspicion surrounding Russia's role in the hack of the Democratic National Committee and the Trump campaign's rhetoric about withdrawing support for Eastern European NATO allies in the face of Russian aggression.
    '''


if __name__ == '__main__':
    config = readConfig()

    for mail_to in config['mailto_list']:
        for mail_user in config["mail_users"]:
            for i in range(0, 30):
                if send_mail(mail_server, mail_user["name"], mail_user['pass'], mail_to, "Top Stories", generateContent()):
                    print("发送成功")
                else:
                    print("发送失败")

                time.sleep(30)
