import os
import re
import ssl

import requests

from spider import common
from spider.server import oss_service


# ssl._create_default_https_context = ssl._create_unverified_context


# def urllib_download(url):
#     headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
#     r = requests.get(url, headers=headers, stream=True)
#     print(r.status_code)  # 返回状态码
#     if r.status_code == 200:
#         folder_path = '/Users/developer/Desktop/cache/img'
#         if not os.path.exists(folder_path):
#             os.makedirs(folder_path)
#         open(folder_path + '/test', 'wb').write(r.content)  # 将内容写入图片
#         print("done")
#     del r
#
#
# def download_from_url(url):
#     start = common.get_current_time()
#     headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
#     resp = requests.get(url, headers=headers, timeout=1)
#
#     print("resp.content = ", len(resp.content))
#     print("Content-Length = ", resp.headers['Content-Length'])
#     oss_key = oss_service.upload_to_oss('test22222.jpg', resp)
#     end = common.get_current_time()
#     print("rt = ", end - start)


if __name__ == '__main__':
    str = '''<div class="markdown-body cache"><style>.markdown-body{color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%}.markdown-body p{color:#595959;font-size:15px;line-height:2;font-weight:400}.markdown-body p+p{margin-top:16px}.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6{padding:30px 0;margin:0;color:#135ce0}.markdown-body h1{position:relative;text-align:center;font-size:22px;margin:50px 0}.markdown-body h1:before{position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)}.markdown-body h2{position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0}.markdown-body h3{font-size:16px}.markdown-body ul{list-style:disc outside;margin-left:2em;margin-top:1em}.markdown-body li{line-height:2;color:#595959}.markdown-body img.loaded{margin:0 auto;display:block}.markdown-body blockquote{background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5}.markdown-body blockquote p{color:#666;line-height:2}.markdown-body a{color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none}.markdown-body em strong,.markdown-body strong{color:#036aca}.markdown-body hr{border-top:1px solid #135ce0}.markdown-body pre{overflow:auto}.markdown-body code,.markdown-body pre{overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace}.markdown-body pre>code{font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8}.markdown-body code{word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em}.markdown-body table{border-collapse:collapse;margin:1rem 0;overflow-x:auto}.markdown-body table td,.markdown-body table th{border:1px solid #dfe2e5;padding:.6em 1em}.markdown-body table tr{border-top:1px solid #dfe2e5}.markdown-body table tr:nth-child(2n){background-color:#f6f8fa}</style><style data-highlight="">.markdown-body pre,.markdown-body pre>code.hljs{color:#333;background:#f8f8f8}.hljs-comment,.hljs-quote{color:#998;font-style:italic}.hljs-keyword,.hljs-selector-tag,.hljs-subst{color:#333;font-weight:700}.hljs-literal,.hljs-number,.hljs-tag .hljs-attr,.hljs-template-variable,.hljs-variable{color:teal}.hljs-doctag,.hljs-string{color:#d14}.hljs-section,.hljs-selector-id,.hljs-title{color:#900;font-weight:700}.hljs-subst{font-weight:400}.hljs-class .hljs-title,.hljs-type{color:#458;font-weight:700}.hljs-attribute,.hljs-name,.hljs-tag{color:navy;font-weight:400}.hljs-link,.hljs-regexp{color:#009926}.hljs-bullet,.hljs-symbol{color:#990073}.hljs-built_in,.hljs-builtin-name{color:#0086b3}.hljs-meta{color:#999;font-weight:700}.hljs-deletion{background:#fdd}.hljs-addition{background:#dfd}.hljs-emphasis{font-style:italic}.hljs-strong{font-weight:700}</style><blockquote>
<p>稻盛和夫</p>
</blockquote>
<img alt="center" align="center" width="90%" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a008ecc5410c4df09c7309cd571dd0a0~tplv-k3u1fbpfcp-zoom-in-crop-mark:3024:0:0:0.image?" loading="lazy">
<h1 data-id="heading-0">一句话总结</h1>
<p>人活在世，不可避免地要工作。既然无法选择不工作那不如爱上自己所从事的工作，树立积极向上的劳动观，付出自己的热情并充分发挥自己的能力。通过劳动改变自己的人生轨迹。最后：人生.工作的结果 = 思维方式 x 热情 x 能力。</p>
<h1 data-id="heading-1">脑图</h1>
<img alt="center" align="center" width="90%" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45e684ab47d44f8499b8b2da541e2d1f~tplv-k3u1fbpfcp-zoom-in-crop-mark:3024:0:0:0.image?" loading="lazy">
<h1 data-id="heading-2">详情</h1>
<h2 data-id="heading-3">译者序：热爱的力量</h2>
<blockquote>
<p>曹岫云</p>
</blockquote>
<p>《干法》重点不是讲述具体的工作方法，而是强调人生中的劳动观、工作观，这些观点具有重大而深刻的现实意义。
个人理解：现在社会越来越浮躁，很多年轻人以不劳而获、投机取巧作为正确的价值导向，这种价值观既不长远也不符合常识。调整心态，爱上自己所从事的职业，树立正确的劳动观才能走的稳且远。</p>
<ul>
<li><strong>热爱导致成功</strong>想获得人生及事业的成功，必须热爱自己的职业，哪怕是强迫自己改变也需要爱上自己的职业。热爱自己的工作才能主观地全身心投入，这些投入必然会拿到良好的结果，这些好的结果以及工作态度会获得周围人的肯定，这些肯定会产生自信并激励你更加投入地工作，从而形成良性循环</li>
<li><strong>热爱燃起激情</strong>热爱产生的激情能促使人乐此不疲地工作并产生好的结果</li>
<li><strong>热爱激发灵感</strong>热爱能让人长时间、主观地把精力放到某件事上，时间长了自然能产生突破困难的灵感</li>
<li><strong>热爱陶冶人格</strong>“工作造就人格”，全身心地投入到当前自己该做的事情中，聚精会神、精益求精，可以造就自己深沉厚重的人格；用真挚的态度，正面面对生活、工作、经营中的现实问题，绝不逃避，<strong>这个过程本身就是在提高心性</strong></li>
<li><strong>热爱获得天助:</strong> 天道酬勤，努力过后天意也会帮助你(这个有点玄学~~~)</li>
</ul>
<h2 data-id="heading-4">前言：幸福工作法</h2>
<h3 data-id="heading-5">为了度过有价值的人生</h3>
<p>在经历了战后经济高速发展后日本这个国家迎来了“没有方向的时代”（其实我国也一样）。人们对于“劳动”观念的扭曲以及对“工作”的认知改变正在导致价值观的混乱。越来越多的年轻人不喜欢工作，尽可能逃避工作的责任，不想受企业的约束，只重视私人活动的时间。本身不喜欢自己的工作但是为了糊口又不得不工作，在这种矛盾的驱使下，年轻人戾气越来越重。稻盛想告诉大家的是：<strong>劳动可以给人生带来特别巨大的收获，帮助你度过有价值的人生。</strong></p>
<h3 data-id="heading-6">工作是“万病良药”</h3>
<p>工作是万病良药，通过工作你可以克服各种困难与考验，让自己的人生时来运转。（个人理解：工作工作的锻炼，你可以练就良好的处事态度与能力，这些通用的能力在生活中同样用得上，这些能力会帮你改变人生的轨迹）</p>
<h2 data-id="heading-7">第1章：为什么要工作？磨练灵魂，提升心志</h2>
<p>个人感悟：工作中有大量的机会锻炼一个人的处事态度、行为方式。如果能正确、全神贯注地处理工作就能练就一套通用的处世哲学，这套理论体系在生活里随处都可用得到，有了这些通用的能力就能抓住机会改变人生轨迹。</p>
<h3 data-id="heading-8">1.1 我们为什么而工作</h3>
<p><strong>人工作的目的应该是磨炼自己的心志。只有通过长时间不懈的工作，磨砺了心志，才会具备厚重的人格，在生活中沉稳不摇摆。</strong></p>
<h3 data-id="heading-9">1.2 工作造就人格</h3>
<ul>
<li>劳动的意义不仅在于业绩，更在于完善人的内心。全身心地投入当前自己该做的事情中去，聚精会神，精益求精，这样做本身就是在耕耘自己的心田，可以造就自己深沉厚重的人格</li>
<li>正确的劳动观：劳动是既能磨炼技能，又能磨炼心志的修行，劳动应该被看成自我实现，完善人格的道场</li>
</ul>
<h3 data-id="heading-10">1.3 “极度”认真地工作能扭转人生</h3>
<p>很多人不喜欢自己的工作，不停地想通过换工作去找到自己热爱的工作，但是往往换工作后又面临着跟现在工作相同的处境。稻盛和夫大学毕业后进入即将倒闭的“京瓷”也面临着同样的困惑从而不停地发牢骚，但是他及时扭转了自己的心态，极度认真的工作并从工作中找到了乐趣(经过枯燥的研究，他获得了一次又一次的成果)，从而形成了良性循环，扭转了人生</p>
<h3 data-id="heading-11">1.4 那些智慧迸发的瞬间</h3>
<p>讲述了作者在“京瓷”研究新型陶瓷材料的时候，在尝试了多种方式都没有成功时，突然被脚下的松香绊了一跤，从而借助松香成功研发了新型材料的故事。</p>
<ul>
<li>努力后自有天助：即使在苦难当中，只要拼命工作，就能带来不可思议的好运</li>
<li>阳光总在风雨后：不体验痛苦与烦恼，人们就很难有大的发展，也不会抓住真正的幸福。(经过大风大浪的人才能把握住机会)</li>
<li><strong>顺境也好，逆境也罢，不管自己处在何种境遇，都要抱着积极的心态朝前看，任何时候都要拼命、持续努力，这才是最重要的</strong></li>
</ul>
<h3 data-id="heading-12">1.5 努力工作的彼岸是美好人生</h3>
<p>没有目标，每天吃喝玩乐，长此以往，不但不会成长还会丧失人性中的那些美好（个人理解:没有目标的人即使有钱也不会快乐，况且你还没钱~~~）</p>
<h3 data-id="heading-13">1.6 坚持“愚直地、认真地、诚实地”工作</h3>
<p><strong>一心一意地投身于工作，聚精会神，孜孜不倦，精益求精，这本身就是磨炼人格的修行。通过这种心志的提升，每个人的人生价值也会随着提升</strong></p>
<h3 data-id="heading-14">1.7 要每天反省</h3>
<p>人生中，要提升心志，说起来容易做起来难。</p>
<ul>
<li>**不断reivew：**对今天做过的事，老老实实进行反省，发誓从明天起认真改进，这样度过反省的每一天，我们不但能避免工作上的失败，还能提升心志。</li>
</ul>
<h2 data-id="heading-15">第2章：如何投入工作？让自己喜欢上所从事的工作</h2>
<p>个人感悟：学习自己喜欢的专业、从事自己喜欢的职业、做自己喜欢的方向，这些概率都太低了。及时调整心态，主动拥抱自己的工作，才能找到“天职”</p>
<h3 data-id="heading-16">2.1 改变心态</h3>
<p>爱上喜欢的工作从调整心态开始：“天职”不是偶然碰上的，而是自己亲自制造出来的。</p>
<h3 data-id="heading-17">2.2 “迷恋”工作</h3>
<p><strong>喜欢自己的工作——仅此一条就能决定一个人的一生。</strong>
喜欢自己工作才能形成良性循环：</p>
<img alt="center" align="center" width="50%" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/438417630df849e8a01de6776d27476a~tplv-k3u1fbpfcp-zoom-in-crop-mark:3024:0:0:0.image?" loading="lazy">
<h3 data-id="heading-18">2.3 感动给人注入新的动力</h3>
<p><strong>常怀感动之心</strong>如果只是当苦行僧，一味地强调吃苦耐劳但是没有快乐，很难持之以恒。因此必须从工作中寻找快乐——降低快乐的门槛，小的事情也可以很快乐，把这些快乐转化成精神食粮继续投入到艰苦的工作中</p>
<h3 data-id="heading-19">2.4 抱着产品睡</h3>
<p>给产品注入深沉的关爱之情才能把事情做出色</p>
<h3 data-id="heading-20">2.5 倾听“产品的哭泣声”</h3>
<p>如果你能喜欢上你的工作，喜欢上自己制造的产品，那么当问题发生时，你一定能找到解法（前提是你注入了大量的热情及喜欢，无时无刻不关注产品）
当工作迷失方向时，你的产品会让你倾听到他的“窃窃私语”，帮你找到解决问题的线索，让你的事业开始起飞。</p>
<h3 data-id="heading-21">2.6 成为“自燃型”的人</h3>
<p>自然界中材料可以分成三种：自燃、可燃、不燃。人也是一样。自燃型的人是强自我驱动型，在“别人吩咐之前自发去干”，而不是“有了命令才去干”</p>
<h3 data-id="heading-22">2.7 勇于在“旋涡中心”工作</h3>
<p>勇于成为工作中的“领头羊”</p>
<h2 data-id="heading-23">第3章：以高目标为动力——持续付出不亚于任何人的努力</h2>
<p>人本来就具备使梦想成真的巨大潜力</p>
<h3 data-id="heading-24">3.1 不断树立“高目标”</h3>
<p>纵使是自不量力的梦想，看似高不可攀的目标，也要牢牢树立这个目标并坚持在同仁面前展示这个目标(如果你当老板的话~)。高目标是促使个人与组织进步的最大动力</p>
<h3 data-id="heading-25">3.2 首先“必须得想”</h3>
<p>文中介绍了日本“经营之神”——松下幸之助的“水库哲学”：企业经营的过程中时刻要保留一定的现金储备。很多人对此不屑一顾，他们希望得到一些具体的方法去经营自己的企业。但是“企业要有盈余”这个目标的实现思路每个企业都不一样，有目标后要敢于想象并千方百计去达成才有意义。
<strong>有目标之后要敢于想，千法百计想办法去实现，否则什么都做不成，这对个人与企业来说是铁则</strong></p>
<h3 data-id="heading-26">3.3 把愿望渗透到“潜意识”</h3>
<blockquote>
<p>潜意识是指不自觉的就会这么干，形成习惯的意识。比如老司机开车的时候，什么路况做什么操作就是一种潜意识</p>
</blockquote>
<p>要实现高目标，前提就是不断持续地怀抱能渗透到“潜意识”的强烈愿望。</p>
<h3 data-id="heading-27">3.4 当你竭尽全力时，神灵将会现身</h3>
<p>“尽人事，听天命”肯定会有好结果。但是前提是真正的将努力付出到极致，真正的“尽了人事”</p>
<h3 data-id="heading-28">3.5 付出“不亚于任何人的努力”乃是自然的机理</h3>
<p>很多人一提“不亚于任何人的努力”往往是一个沉重的话题，意味着自己没有休息时间，意味着被压榨。但是这却是一个自然机理，文中举了马路上的小草，顶着炎炎夏日与混凝土的重量艰难生长、生根发芽的例子说明“努力”是一个自然机理，不仅仅在人类身上体现（自然界的优胜劣汰适者生存）。</p>
<h2 data-id="heading-29">第4章：持续就是力量——抓紧今天这一天</h2>
<p><strong>看起来平凡、不起眼的工作能坚韧不拔地去做，坚持不懈地去做，这种持续的力量才是成功的基石。</strong></p>
<h3 data-id="heading-30">4.1 持续地力量能将“平凡”变为“非凡”</h3>
<ul>
<li>所谓人生就是一瞬间、一瞬间持续的积累。每一秒的积累组成了人的一生。同时，伟大的事业也是“枯燥”工作的积累，如此而已。</li>
<li>工作中有两种人：豹子一样行为敏捷的人、牛一样愚直的人。往往坚持到最后成功的是牛一样的人。
<ul>
<li>笨并不可怕，要用发展的眼光看待自己，持续地努力可以将平凡变成非凡。</li>
</ul>
</li>
</ul>
<h3 data-id="heading-31">4.2 比昨天更进一步</h3>
<p>每天前进一点点，日积月累，你将变成参天大树</p>
<h3 data-id="heading-32">4.3 抓紧今天这一天</h3>
<p>从心理学的角度看：如果达成目标的时间过长，往往中途就会遭遇挫折。遭遇挫折难免会泄气。与其中途要作废，不如不指定过于远大的计划，将未来一年的规划细化成每个月、每一天然后千方百计达成。这样每个瞬间都会非常充实，小的成就连绵不断无限持续，这样，乍一看远大的目标就一定能实现</p>
<h3 data-id="heading-33">4.4 能力要用“将来进行时”</h3>
<p>作者主张：在建立目标时，要设定“超出自己能力之上的指标”
<strong>人的能力有无限延伸的可能，用动态的眼光看待自己，拒绝自我否定、畏难，坚信自己将来一定能行，然后不断提高自己，就能实现现在看起来遥不可及的目标</strong></p>
<h3 data-id="heading-34">4.5 “已经不行了”的时候才是真正的开始</h3>
<p>已经不行了绝对不是终点，而是新的起点。人需要具备一定的韧性(就像原始狩猎民族的狩猎之旅一样)，在成功之前不屈不挠，坚韧不拔。不给自己设限，持续挑战，转危为安</p>
<h3 data-id="heading-35">4.6 苦难与成功都是考验</h3>
<p>胜不骄败不馁，每天勤奋工作比什么都重要</p>
<h3 data-id="heading-36">4.7 不要有感性的烦恼</h3>
<p><strong>永远不要后悔：如果失败了就对失败的原因进行分析，诚恳反省。当你做完了充分的反思之后就要把这件事情忘掉。不管工作还是生活不可能事事顺心，不要纠结在失败中无法自拔</strong></p>
<h3 data-id="heading-37">4.8 哪怕险峻高山，也要垂直攀登</h3>
<p>**直面困难，不要畏缩：**就像爬山一样，即使面前是险峻高山，也要垂直攀登。如果采取安全的办法人就会产生“理想归理想，现实是现实”的妥协想法。一旦妥协必定放弃之前的目标。</p>
<h2 data-id="heading-38">第5章：怎样才能出色工作——追求完美主义</h2>
<h3 data-id="heading-39">5.1 出色的工作产生于“完美主义”</h3>
<ul>
<li>经过平时的不断训练，养成习惯后工作中就能做到“有意注意”。与“有意注意”相对的是“无意注意”(比如车间中机器坏了，大家才知道保养)，有意注意体现的是预先知道问题的能力</li>
<li>不论做什么事情都能贯彻“有意注意”，那么不仅仅能大幅降低差错与失误，问题出现时还能快速抓住问题的本质并予以解决</li>
</ul>
<h3 data-id="heading-40">5.2 橡皮绝对擦不掉的错误</h3>
<p>无论任何事情，“错了改改就行”的想法绝对不能有。平时就要用心做到有意注意，不允许发生任何差错，贯彻这种完美主义才能提高工作质量与自身素质。（虽然严苛到bt，这也许就是世界顶流的思考者的哲学吧）</p>
<h3 data-id="heading-41">5.3 最重要的是“注重细节”</h3>
<p>做“会划破手的”产品(ps: 遇到一件完美无暇的东西，小孩冒失地去碰的时候母亲就会告诉他这个会划破手，这里形容精致、完美的产品)</p>
<h3 data-id="heading-42">5.4 事先“看见完成时的状态”就定能成功</h3>
<p>**有想法，有步骤：**想要成就某项事业，要时时刻刻描绘这一事业的理想状态。同时对实现这个理想的过程也要反复思考，直到看得见为止</p>
<h3 data-id="heading-43">5.5 抓住一切机会磨炼“敏锐度”</h3>
<p>“敏锐度”是事事用心才能练就的，这种敏锐度是“有意注意”的前提。有了这种敏锐度才能在问题发生之前发现“不对头”并迅速采取对策</p>
<h3 data-id="heading-44">5.6 不是“最佳”而是“完美”</h3>
<p>本章标题所谓的“完美主义”不是更好，而是至高无上。
最佳是一个比较词，是有同类产品中比较出来的。完美不是比较出来的，是一种至高无上的完美主义。</p>
<h2 data-id="heading-45">第6章：创造性工作——每天都要钻研创新</h2>
<p>“不满足于现状”、“总想做的更好”、“总想不断提高自己” ，有没有这种想法也许是“成功”或“失败”差距的根源</p>
<h3 data-id="heading-46">6.1 敢于走别人没走过的路</h3>
<p><strong>干别人干过的事很难获得出色的成果，因为大多数人走过的路上不会剩下什么有价值的东西。无人涉足的新路，尽管寸步难行，却可以有许多新的发现与巨大的成果</strong></p>
<h3 data-id="heading-47">6.2 扫地改变人生</h3>
<blockquote>
<p>文中介绍了扫地的案例：在车间中扫地是一件极其微不足道的工作，每天都是从头往后扫。是不是需要尝试一下从中间往两边扫？是不是可以采用自动化的方式买个扫地机器人？是不是可以通过扫地机器人的改良扫的更干净？如果采用了你的方式扫的更干净是不是可以自己开一家扫地公司？</p>
</blockquote>
<p><strong>无论多么渺小的工作，都积极去做，抱着问题意识开动脑筋对现状进行改良。有这种想法的人与没有这种想法的人时间久了会差的越来越大</strong></p>
<h3 data-id="heading-48">6.3 外行的长处是可以自由发想</h3>
<p><strong>成就伟大事业的往往不是领域的专家而是不被任何成见束缚的“外行”，我们也不应该给自己设限，要积极地去挑战新事物。</strong></p>
<h3 data-id="heading-49">6.4 既然定了计划，就一定要实现</h3>
<p>制定了计划，就要使用强烈的愿望与高尚的思想不断描绘内心的蓝图并激励自己去实现
<strong>人们的思想、愿望中蕴藏着巨大的能量！</strong></p>
<h3 data-id="heading-50">6.5 乐观构思、悲观计划、乐观执行</h3>
<p>向新课题发起挑战的最好方法：</p>
<ul>
<li>乐观构思：不要畏难，乐观描绘将来的蓝图，不要觉得目标不可能</li>
<li>悲观计划：详细地思考构思的实施方式，将潜在的问题以及可能遇到的困难提前识别出来，谨慎地建立起行动计划</li>
<li>乐观执行：计划一旦进入实施阶段，就要果断、乐观地执行，不能再悲观</li>
</ul>
<h2 data-id="heading-51">结语：人生.工作的结果 = 思维方式 x 热情 x 能力</h2>
<p>人生.工作的结果 = 思维方式 x 热情 x 能力。</p>
<ul>
<li>思维方式(分数:-100 - +100): 积极、不厌辛劳、愿意付出的思维方式是+100分；消极、怨天尤人、愤世嫉俗的思维方式是-100分。这个因素可以通过后天主观改变</li>
<li>热情(分数:0-100)：热情又称为努力。缺乏干劲、懒散潦倒的人得分0；对工作充满火焰般热情的人得分100。这个因素可以通过后天主观改变</li>
<li>能力(分数:0-100)：智力、运动神经或者健康等天赋，体弱多病的人比健康的人得分低。这个是与生俱来的基本不可通过后天改变</li>
</ul>
<h2 data-id="heading-52">附录</h2>
<ul>
<li><strong>永远不要奢侈，一旦奢侈就会傲慢</strong></li>
</ul>
<hr>
<p><strong>欢迎大家微信扫下面二维码，关注我的公众号【趣code】，一起成长~</strong></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/84c8f49430164c1daba547fb0edc1482~tplv-k3u1fbpfcp-zoom-in-crop-mark:3024:0:0:0.image?" alt="扫码_搜索联合传播样式-白色版.png" loading="lazy"></p></div>'''
urls = re.findall('img[\s\S]+?src=[\'\"](.*?)[\'\"]', str, re.S)
print(urls)
for url in urls:
    print(url)
    # urllib_download("https://s2.loli.net/2023/03/05/qigmFrL4U7I5WbA.png")
