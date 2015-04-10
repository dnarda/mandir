<!doctype html>
<html>
<head>
    {% load staticfiles %}

    {% block titlename %}
        <title>Welcome to Ved Mandir</title>
    {% endblock %}

    <link rel="stylesheet" href="{% static "css/bootstrap-theme.min.css" %}">
    <script src="{% static "js/jquery-1.11.2.min.js" %}"></script>
    <script src="{% static "js/bootstrap.js" %}"></script>



	<link rel="stylesheet" href="http://fonts.googleapis.com/css?family=Open+Sans:400italic,400">
	<link rel="stylesheet" href="http://fonts.googleapis.com/css?family=Droid+Sans">
	<link rel="stylesheet" href="http://fonts.googleapis.com/css?family=Lobster">
	<link rel="stylesheet" href="{% static "css/prettyPhoto.css" %}">
	<link rel="stylesheet" href="{% static "css/flexslider.css" %}">
	<link rel="stylesheet" href="{% static "css/font-awesome.css" %}">
	<link rel="stylesheet" href="{% static "css/style.css" %}">
	<link rel="shortcut icon" href="http://gahlot.us/VedMandir2/favicon.ico" type="image/x-icon">
	<link rel="icon" href="http://gahlot.us/VedMandir2/favicon.ico" type="image/x-icon">

	<!-- HTML5 shim, for IE6-8 support of HTML5 elements -->
	<!--[if lt IE 9]>
		<script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
	<![endif]-->

	<!-- Favicon and touch icons -->
	<link rel="shortcut icon" href="{% static "ico/favicon.ico" %}">
	<link rel="apple-touch-icon-precomposed" sizes="144x144" href="{% static "ico/apple-touch-icon-144-precomposed.png" %}">
	<link rel="apple-touch-icon-precomposed" sizes="114x114" href="{% static "ico/apple-touch-icon-114-precomposed.png" %}">
	<link rel="apple-touch-icon-precomposed" sizes="72x72" href="{% static "ico/apple-touch-icon-72-precomposed.png" %}">
	<link rel="apple-touch-icon-precomposed" href="{% static "ico/apple-touch-icon-57-precomposed.png" %}">


    {% block extra_styles %}

    {% endblock %}

</head>

<body>
    <div class="container main-container"
         style="width:100%; background-color:white; margin: 0;padding: 0 15px 10px 15px; min-height:80vh;" id="#main-container">

        <div class="container">
            <div class="header row">
                <div class="span12">
                    <div class="navbar">
                        <div class="navbar-inner">
                            <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
                                <span class="icon-bar"></span>
                                <span class="icon-bar"></span>
                                <span class="icon-bar"></span>
                            </a>
                            <h1>
                                <a class="brand" href="ved/index.html">Ved Mandir</a>
                            </h1>
                            <div class="nav-collapse collapse">
                                <ul class="nav pull-right">
                                    <li class="current-page">
                                        <a href="ved/index.html"><i class="icon-home"></i><br />Home</a>
                                    </li>
                                    <li>
                                        <a href="ved/services.html"><i class="icon-tasks"></i><br />Events</a>
                                    </li>
                                    <li>
                                        <a href="ved/portfolio.html"><i class="icon-camera"></i><br />Darshan</a>
                                    </li>
                                    
                                    <li>
                                        <a href="ved/photos.html"><i class="icon-camera"></i><br />Photos</a>
                                    </li>
                                     <li>
                                        <a href="ved/vol.html"><i class="icon-comments"></i><br />Volunteer</a>
                                    </li>
                                  
                                    <li>
                                        <a href="ved/hall.html"><i class="icon-book"></i><br />Temple Hall <br /> Availability</a>
                                    </li>
 
                                    <li>
                                        <a href="ved/contact.html"><i class="icon-envelope-alt"></i><br />Contact</a>
                                    </li>
                                     <li>
                                        <a href="ved/about.html"><i class="icon-user"></i><br />About</a>
                                    </li>
                                    
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        {% block content %}


        {% endblock %}

    </div>
</body>

