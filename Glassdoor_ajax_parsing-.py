import re

from flask import Flask
import requests, random, time
from bs4 import BeautifulSoup as bs
from bs4 import NavigableString, Comment
from pprint import pprint


app = Flask(__name__)


url = "https://www.glassdoor.com/Job/python-jobs-SRCH_KO0,6.htm?includeNoSalaryJobs=true&p=2"
headers = {
    'accept-encoding': 'gzip, deflate, br',
    # "Accept": "image/avif,image/webp,*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/94.0.4606.81 Safari/537.36",
    # 'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8',
    # 'apollographql-client-name': 'job-search',
    # 'apollographql-client-version': '0.13.12',
    # 'at': 'undefined',
    # 'content-length': '5825',
    # 'content-type': 'application/json',
    'cookie': 'gdId=a1d6c0f2-2e27-40a2-ae66-2df8d9d419f3; trs=direct:direct:direct:2021-10-25+12%3A16%3A31.63:undefined:undefined; indeedCtk=1fise418eu5dk801; _gid=GA1.2.1331093537.1635189398; _optionalConsent=true; _gcl_au=1.1.67833082.1635189399; _fbp=fb.1.1635189399421.366325899; __gads=ID=d25f399b5c8fb22c-2299095400cb00bf:T=1635189400:S=ALNI_MaGF9YMdEYnjMupC-4tHLtgwvzG4g; G_ENABLED_IDPS=google; ki_r=; fpvc=2; ki_t=1635283654088%3B1635887729069%3B1635887729069%3B6%3B7; JSESSIONID_JX_APP=8885856D4356A84406462EE5FFE83F88; GSESSIONID=a1d6c0f2-2e27-40a2-ae66-2df8d9d419f3+1636004005131; asst=1636004005.0; __cf_bm=iV9Vh.qlEqQVP1bli80J7YmcY5O.KkoF6Osvojrq4Nc-1636004005-0-AYx8aEDBBpocumP/0uwf5/08HqxQBSvI/HppLSVzECz/8es416iZUGCutIJPAzr7ZEHspR+/ByYJANV/Gjxj0PA=; JSESSIONID=00E39AFB8E0C872A295EADE523664938; _GA_Job_Session=true; cass=2; gdsid=1636004005131:1636004389013:19C921DC856AB5C45D013A4A97857D75; _ga=GA1.2.387389572.1635189398; OptanonConsent=isIABGlobal=false&datestamp=Thu+Nov+04+2021+08%3A39%3A54+GMT%2B0300+(Moscow+Standard+Time)&version=6.8.0&hosts=&consentId=e6bfa58b-3c35-420c-bc85-fa6b5451fdbb&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1%2CC0017%3A1&AwaitingReconsent=false; bs=EfJdvDB--J7DvJV3K1qPwA:Hjr8xRWt7TIUQ_kR3xorg9_GZO-x6_ZR9eknrig1P3-gzdEvb8OtbEK7UfRxcgqiz-92IGw9fYdoHvXVoReR8LPtipWLzLUliixrw89mINI:VDd2pODs8Tuat37BHuNc6fee_y2KF3OLXxQu65OSnFI; AWSALB=CX+O18SvCFHdBOexr8NZqPTsqVOvzR1tyFc3JQs1wdI7QTbGV9aflx2fnG3IAR1G7pTMdROuXQevaAE5DugRj+b6aYDhQsoXQNxz6vaTH1w+3V18zfrRm0tbsgBEt0DeamocS8Zelko+3+7tZvKTVWgCWQ3uAdjmVAbgCqM7O+FBbalISo3p1dcAuHFHKw==; AWSALBCORS=CX+O18SvCFHdBOexr8NZqPTsqVOvzR1tyFc3JQs1wdI7QTbGV9aflx2fnG3IAR1G7pTMdROuXQevaAE5DugRj+b6aYDhQsoXQNxz6vaTH1w+3V18zfrRm0tbsgBEt0DeamocS8Zelko+3+7tZvKTVWgCWQ3uAdjmVAbgCqM7O+FBbalISo3p1dcAuHFHKw==; ADRUM_BTa=R:26|g:3653848e-d6ce-46d6-a6ea-e22cc86aafe4|n:glassdoor_17d346a0-2ec1-4454-86b0-73b3b787aee9; SameSite=None; ADRUM_BT1=R:26|i:1188649|e:14|d:4; ADRUM_BT2=R:26|i:1188650|e:140; _ga_RC95PMVB3H=GS1.1.1636004008.33.1.1636004552.60',
    'gd-csrf-token': '4N__gJZSsobTutp_xY890Q:RyAkfm_U7Xp7R5fbOzYcS1iGlXuNyYdc6hdSnvDUwEKOcQsndVwNH4DQMcjJV4cNpJUV5sdfKaKclek1_YjLfw:trmHIO09yyQDFnlmvWfigY3MEA7bQah3tqpcFwA-9Yg',
    # 'origin': 'https://www.glassdoor.com',
    # 'referer': 'https://www.glassdoor.com/',
    # 'sec-ch-ua': '"Microsoft Edge";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
}

data = {
        'operationName': "JobDetailQuery",
        'query': "query JobDetailQuery($jl: Long!, $queryString: String, $enableReviewSummary: Boolean!) {\n  jobView(listingId: $jl, contextHolder: {queryString: $queryString}) {\n    ...DetailFragment\n    employerReviewSummary @include(if: $enableReviewSummary) {\n      reviewSummary {\n        highlightSummary {\n          sentiment\n          sentence\n          categoryReviewCount\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment DetailFragment on JobView {\n  employerBenefits {\n    benefitsOverview {\n      benefitsHighlights {\n        benefit {\n          commentCount\n          icon\n          name\n          __typename\n        }\n        highlightPhrase\n        __typename\n      }\n      overallBenefitRating\n      employerBenefitSummary {\n        comment\n        __typename\n      }\n      __typename\n    }\n    benefitReviews {\n      benefitComments {\n        id\n        comment\n        __typename\n      }\n      cityName\n      createDate\n      currentJob\n      rating\n      stateName\n      userEnteredJobTitle\n      __typename\n    }\n    numReviews\n    __typename\n  }\n  employerContent {\n    featuredVideoLink\n    managedContent {\n      id\n      type\n      title\n      body\n      captions\n      photos\n      videos\n      __typename\n    }\n    diversityContent {\n      goals {\n        id\n        workPopulation\n        underRepresentedGroup\n        currentMetrics\n        currentMetricsDate\n        representationGoalMetrics\n        representationGoalMetricsDate\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  employerAttributes {\n    attributes {\n      attributeName\n      attributeValue\n      __typename\n    }\n    __typename\n  }\n  header {\n    jobLink\n    adOrderId\n    advertiserType\n    ageInDays\n    applicationId\n    appliedDate\n    applyUrl\n    applyButtonDisabled\n    blur\n    coverPhoto {\n      url\n      __typename\n    }\n    divisionEmployerName\n    easyApply\n    easyApplyMethod\n    employerNameFromSearch\n    employer {\n      id\n      name\n      size\n      squareLogoUrl\n      __typename\n    }\n    expired\n    goc\n    hideCEOInfo\n    indeedApplyMetadata\n    indeedJobAttribute {\n      education\n      skills\n      __typename\n    }\n    jobTitleText\n    jobTypeKeys\n    jobCountryId\n    jobResultTrackingKey\n    locId\n    locationName\n    locationType\n    normalizedJobTitle\n    organic\n    payCurrency\n    payPercentile90\n    payPercentile50\n    payPercentile10\n    hourlyWagePayPercentile {\n      payPercentile90\n      payPercentile50\n      payPercentile10\n      __typename\n    }\n    payPeriod\n    rating\n    salarySource\n    savedJobId\n    sgocId\n    sponsored\n    categoryMgocId\n    urgencySignal {\n      labelKey\n      messageKey\n      normalizedCount\n      __typename\n    }\n    __typename\n  }\n  similarJobs {\n    relatedJobTitle\n    careerUrl\n    __typename\n  }\n  job {\n    description\n    discoverDate\n    eolHashCode\n    importConfigId\n    jobReqId\n    jobSource\n    jobTitleId\n    jobTitleText\n    listingId\n    __typename\n  }\n  map {\n    address\n    country\n    employer {\n      id\n      name\n      __typename\n    }\n    locationName\n    postalCode\n    __typename\n  }\n  overview {\n    ceo {\n      name\n      photoUrl\n      __typename\n    }\n    id\n    name\n    shortName\n    squareLogoUrl\n    headquarters\n    links {\n      overviewUrl\n      benefitsUrl\n      photosUrl\n      reviewsUrl\n      salariesUrl\n      __typename\n    }\n    primaryIndustry {\n      industryId\n      industryName\n      sectorName\n      sectorId\n      __typename\n    }\n    ratings {\n      compensationAndBenefitsRating\n      cultureAndValuesRating\n      careerOpportunitiesRating\n      workLifeBalanceRating\n      __typename\n    }\n    overview {\n      description\n      __typename\n    }\n    revenue\n    size\n    type\n    website\n    yearFounded\n    __typename\n  }\n  photos {\n    photos {\n      caption\n      photoId\n      photoId2x\n      photoLink\n      photoUrl\n      photoUrl2x\n      __typename\n    }\n    __typename\n  }\n  rating {\n    ceoApproval\n    ceoRatingsCount\n    employer {\n      name\n      __typename\n    }\n    recommendToFriend\n    starRating\n    __typename\n  }\n  reviews {\n    reviews {\n      advice\n      cons\n      countHelpful\n      employerResponses {\n        response\n        responseDateTime\n        userJobTitle\n        __typename\n      }\n      employmentStatus\n      featured\n      isCurrentJob\n      jobTitle {\n        text\n        __typename\n      }\n      lengthOfEmployment\n      pros\n      ratingBusinessOutlook\n      ratingCareerOpportunities\n      ratingCeo\n      ratingCompensationAndBenefits\n      ratingCultureAndValues\n      ratingOverall\n      ratingRecommendToFriend\n      ratingSeniorLeadership\n      ratingWorkLifeBalance\n      reviewDateTime\n      reviewId\n      summary\n      __typename\n    }\n    __typename\n  }\n  salary {\n    currency {\n      code\n      numOfDecimals\n      negativeFormat\n      positiveFormat\n      symbol\n      __typename\n    }\n    lastSalaryDate\n    salaries {\n      count\n      maxBasePay\n      medianBasePay\n      minBasePay\n      jobTitle {\n        id\n        text\n        __typename\n      }\n      payPeriod\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n",
        'enableReviewSummary': 'true',
        'jl': '1007396212871',
        'queryString': "pos=101&ao=1136043&s=58&guid=0000017ce9785c91a6c36c9346454cfb&src=GD_JOB_AD&t=SR&vt=w&cs=1_97381ad4&cb=1636004553029&jobListingId=1007396212871&jrtk=3-0-1fjkngn6cu5r1801-1fjkngn76u1ad800-71c91f8525fe43a8-"
}

req = requests.get(url, headers=headers, params=data)
with open("index.html", "w", encoding="utf-8") as file:
    file.write(req.text)
print("Index.html created")
soup = bs(req.text, "lxml")

# data = soup.find("article", {"class": "scrollable active", "data-id": "1007390246386"})
# print(data)

# <article class="scrollable active css-1ctl34j ead8scz3" data-id="1007390246386"><div><div class="stuck" style="width: 100%; height: 345px; position: relative;"><div style="position: absolute; top: 0px;"><div style="position: fixed; background-color: white; border-bottom: 1px solid rgb(222, 224, 227); z-index: 2; width: 469.391px;"><div data-brandviews="BRAND:n=jsearch-hero-header:eid=0:jlid=1007390246386" data-test="hero-header-module" class="css-9ml2tt evnfo7p0" data-triggered-brandview=""><div class="css-1h9mu8x e14vl8nk0"><div class="css-dufhjo e1tk4kwz0"><div class="css-xuk5ye e1tk4kwz5">ANGELIKA IWANOW GLOBAL RECRUITMENT</div><div class="css-1j389vi e1tk4kwz2">Web Developer</div><div class="css-56kyx5 e1tk4kwz1">Remote</div><div><span data-test="detailSalary" class="css-1hbqxax e1wijj240"><span class="css-0 e1wijj242"><span class="SVGInline checkmark"><svg class="SVGInline-svg checkmark-svg" xmlns="http://www.w3.org/2000/svg" width="12" height="9" viewBox="0 0 12 9"><path fill="none" stroke="#0CAA41" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" d="M11 1L3.759 8 1 5.333"></path></svg></span>Employer Provided Salary:</span>$70 Per Hour<span data-test="salaryIcon" class="SVGInline greyInfoIcon"><svg class="SVGInline-svg greyInfoIcon-svg" height="14" viewBox="0 0 14 14" width="14" xmlns="http://www.w3.org/2000/svg"><path d="M7 14A7 7 0 117 0a7 7 0 010 14zm0-.7A6.3 6.3 0 107 .7a6.3 6.3 0 000 12.6zm-.7-7a.7.7 0 011.4 0v4.2a.7.7 0 01-1.4 0zM7 4.2a.7.7 0 110-1.4.7.7 0 010 1.4z" fill="#505863" fill-rule="evenodd"></path></svg></span><div class="d-none"></div></span></div></div><div class="d-flex flex-column"><div class=" css-2tc058 e1rlw03b2"><div class="css-1qiyk1j e1rlw03b1"><div class="gdGrid css-u9poo7 e1ikr6bm0"><span class="indeed-apply-widget indeed-apply-button-container indeed-apply-status-not-applied" data-indeed-apply-nobuttonui="true" data-indeed-apply-partnersa="" data-indeed-apply-onapplied="INDEED_CONFIRM_1" data-indeed-apply-jk="d02f3d1367a9bdf3" data-indeed-apply-jobcountry="US" data-indeed-apply-joburl="https://www.glassdoor.com/partner/jobListing.htm?pos=101&amp;ao=1136043&amp;s=58&amp;guid=0000017cdfe61e12ae83835962e14829&amp;src=GD_JOB_AD&amp;t=SR&amp;vt=w&amp;ea=1&amp;cs=1_55913a59&amp;cb=1635843975161&amp;jobListingId=1007390246386&amp;jrtk=3-0-1fjfuc7jsu40t801-1fjfuc7khhigt800-d02f3d1367a9bdf3-" data-indeed-apply-partnerapitoken="7cc68c0d955e00fa10943c90dd4b7316f6c038bd1c0e36b666a064fb53aa9d01" data-indeed-apply-partnermeta="&amp;jobListingId=1007390246386&amp;adOrderId=1136043&amp;purchaseAdOrderId=0&amp;userId=0&amp;userGuid=a1d6c0f2-2e27-40a2-ae66-2df8d9d419f3&amp;pageGuid=0000017cdfe62787b7f6092987d33912&amp;ip=93.85.92.42&amp;dt=1&amp;pt=3&amp;vt=4&amp;locale=en-US&amp;from=glassdoor&amp;asid=a1d6c0f2-2e27-40a2-ae66-2df8d9d419f3.1635843627.0&amp;spn=0&amp;" data-indeed-apply-pingbackurl="https://gdc.indeed.com/conv/orgIndApp?jk=d02f3d1367a9bdf3&amp;ctk=1fise418eu5dk801&amp;astse=546bde020956c476&amp;assa=5117" data-indeed-apply-continueurl="https://www.glassdoor.com/Job/web-jobs-SRCH_KO0,3.htm"><button class="gd-ui-button mr-0 fillMob d-flex align-items-center justify-content-center css-uypuxd e1mdf2m0 css-1dqhu4c" data-test="applyButton" data-easy-apply="true"><span class="css-8zxfjs"><i class="icon-bolt mr-sm"></i><span>Easy Apply</span><i class="hlpr"></i></span></button></span></div><div class="css-sqn9a1 evnfo7p1"><button class="gd-ui-button fillMob save-job-button-1007390246386 css-1wwa95u e1prsu2a0 css-17fxxbf" data-ao-id="1136043" data-job-id="1007390246386" data-save-hook="JOB_SEARCH_PANE" data-saved-job-id="0" data-test="save-button" type="button"><span class="css-8zxfjs"><span class="SVGInline save css-117egp7 css-6mo0su e1prsu2a1"><svg class="SVGInline-svg save-svg css-117egp7-svg css-6mo0su-svg e1prsu2a1-svg" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M12 5.11l.66-.65a5.56 5.56 0 017.71.19 5.63 5.63 0 010 7.92L12 21l-8.37-8.43a5.63 5.63 0 010-7.92 5.56 5.56 0 017.71-.19zm7.66 6.75a4.6 4.6 0 00-6.49-6.51L12 6.53l-1.17-1.18a4.6 4.6 0 10-6.49 6.51L12 19.58z" fill="currentColor" fill-rule="evenodd"></path></svg></span><span>Save</span></span></button></div><div class="css-1d5xcfh e1p6mryr0"><div class="css-wvg788 exflef10"><span class="SVGInline css-1cqi1eb e1p6mryr3"><svg class="SVGInline-svg css-1cqi1eb-svg e1p6mryr3-svg" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="36" height="36" viewBox="0 0 36 36"><defs><path id="prefix__aMoreDropdown" d="M7.8 20.8a2.8 2.8 0 110-5.6 2.8 2.8 0 010 5.6zm10.2 0a2.8 2.8 0 110-5.6 2.8 2.8 0 010 5.6zm10.2 0a2.8 2.8 0 110-5.6 2.8 2.8 0 010 5.6z"></path></defs><g fill="none" fill-rule="evenodd"><mask id="prefix__bMoreDropdown" fill="#fff"><use xlink:href="#prefix__aMoreDropdown"></use></mask><use fill="#1861bf" xlink:href="#prefix__aMoreDropdown"></use><g mask="url(#prefix__bMoreDropdown)"><path d="M0 0h36v36H0z"></path></g></g></svg></span><span class="hideHH css-q0sxds exflef11">More</span></div></div></div><div class="css-12cg9z e9i34c90"></div></div></div></div></div><div class="" id="SerpFixedHeader" style="width: 100%;"><div><div data-test="scrollable-tabs" class="css-2tnbgt ef7s0la1"><div data-item="tab" data-test="job" data-tab-type="job" data-brandviews="" class="css-uvqkew ef7s0la0" data-triggered-brandview=""><span>Job</span></div><div data-item="tab" data-test="salary" data-tab-type="salary" data-brandviews="" class="css-1ap6ha9 ef7s0la0"><span>Salary</span></div></div></div></div></div></div></div><div class="css-r7fjfn ead8scz1"><div class=" css-15k9b95 elvm8840"><div><div id="JobDescriptionContainer" class="p-std css-1k5huso e856ufb7"><div id="JobDesc1007390246386" class="css-1xdhyk6 e856ufb0"><div class="jobDescriptionContent desc"><div><p>For our Client, an international company engaged in the innovative consumer brands of tomorrow through creativity, data driven results, and omni-channel strategies. Promote their products mainly through Amazon as well as their own Shopify sites and other marketplaces.</p><p></p><p><br>
# Currently we are looking for an outstanding <b>Web Developer</b> to be responsible for the coding, innovative design and layout of ecommerce hub brand. Web developer responsibilities include building our website from concept all the way to completion from the bottom up, fashioning everything from the home page to site layout and function.</p><p></p><p><b><br>
# This is a Full time position</b></p>
# <p><b>
# Annual Salary: 70 000- 120 000 USD</b></p>
# <p><b>
# Remote position</b></p><br>
# <p><b>
# The duties are:</b></p>
# <ul><li><p>
# Write well designed, testable, efficient code by using best software development practices</p></li><li><p>
# Create website layout/user interface by using standard HTML/CSS practices</p></li><li><p>
# Integrate data from various back-end services and databases</p></li><li><p>
# Gather and refine specifications and requirements based on technical needs</p></li><li><p>
# Create and maintain software documentation</p></li><li><p>
# Be responsible for maintaining, expanding, and scaling our site</p></li><li><p>
# Stay plugged into emerging technologies/industry trends and apply them into operations and activities</p></li><li><p>
# Cooperate with web designers to match visual design intent</p></li></ul><p></p><p><b><br>
# Required Knowledge and Skills:</b></p>
# <ul><li><p>
# Proven working experience in web programming</p></li><li><p>
# Top-notch programming skills and in-depth knowledge of modern HTML/CSS</p></li><li><p>
# Top-notch experience with Javascript</p></li><li><p>
# A solid understanding of how web applications work including security, session management, and best development practices</p></li><li><p>
# Aggressive problem diagnosis and creative problem solving skills</p></li><li><p>
# Strong organizational skills to juggle multiple tasks within the constraints of timelines and budgets with business acumen</p></li><li><p>
# Ability to work and thrive in a fast-paced environment, learn rapidly and master diverse web technologies and techniques.</p></li></ul></div></div></div><div class="css-t3xrds e856ufb2">Show Less  <span class="SVGInline"><svg class="SVGInline-svg" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M20.6 14.75l-7.386-7.523a1 1 0 00-1.428 0L4.4 14.75c-.5.509-.5 1.324 0 1.833a1.261 1.261 0 001.8 0l6.3-6.416 6.3 6.416a1.261 1.261 0 001.8 0c.5-.509.5-1.324 0-1.833z" fill-rule="evenodd" fill="currentColor"></path></svg></span></div></div></div><div><div class="salaryTab tabSection p-std"><div class="css-1mvn55c e2u4hf110"><h4 class="css-42mj1f e2u4hf19">Average Base Salary Estimate</h4><div class="css-8djxzr e2u4hf10"><span class="SVGInline"><svg class="SVGInline-svg" style="width: 18px;height: 18px;" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><g fill="currentColor" fill-rule="evenodd"><path d="M15.54 9.24l-5 4.78-2-1.78a.88.88 0 00-1.21 0 .8.8 0 000 1.16l2.63 2.36a.88.88 0 001.21 0l5.66-5.36a.8.8 0 000-1.16.88.88 0 00-1.29 0z"></path><path d="M12 3a9 9 0 109 9 9 9 0 00-9-9zm0 17a8 8 0 118-8 8 8 0 01-8 8z"></path></g></svg></span>Estimate provided by employer</div><div class="css-75grs3 e2u4hf16"><div class="css-y2jiyn e2u4hf18">$16.62<span>&nbsp;/hr (est.)</span></div><div class="d-flex flex-column css-1ff36h2 e2u4hf17"><div class="css-zppf1y e2u4hf14"></div><div class="css-1xcne3f e2u4hf15"></div><div class="d-flex justify-content-between mt-sm"><span class="css-1d4p0fd e2u4hf13">$16.62<span>&nbsp;/hr</span></span><span class="css-1d4p0fd e2u4hf13">$16.62</span></div></div></div><div class="css-1wlcjsj e2u4hf12">When employers manage their jobs on Glassdoor, they have the option to specify an “Employer Estimate” salary range, which replaces any estimate generated by Glassdoor that might otherwise have been associated with this job. If you’d like to learn more about how we calculate “Glassdoor Estimates” when we do not have a salary range provided by the employer, please see the FAQ below.<span data-test="show-more" class="css-1467g58 e2u4hf11">Show More</span></div></div><div class="center"><a rel="noopener noreferrer" target="_blank" class="css-rfjukq e2u4hf111">See All ANGELIKA IWANOW GLOBAL RECRUITMENT Salaries<span class="SVGInline"><svg class="SVGInline-svg" style="width: 15px;height: 15px;" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M16.72 11.29L9.19 3.9a1.3 1.3 0 00-1.83 0 1.26 1.26 0 000 1.78L13.78 12l-6.42 6.3a1.26 1.26 0 000 1.78 1.3 1.3 0 001.83 0l7.53-7.39a1 1 0 000-1.4z" fill="currentColor" fill-rule="evenodd"></path></svg></span></a></div></div></div></div><div class="py-sm css-19plimm e3irv60" data-test="JobDetailsFooter"><div></div><div><span class="minor minorLink css-pl1lro e1q8yazb0">View Data as Table</span>&nbsp;&nbsp;<div class="css-12cg9z e9i34c90"><button class="minorLink showReportJobForm css-uyoqng e10d83g50">Report this job</button></div></div></div></div></div></article>


@app.route('/')
def hello_world():
    pass

if __name__ == '__main__':
    app.run()