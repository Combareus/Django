var script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-3.6.3.min.js'; // Check https://jquery.com/ for the current version
document.getElementsByTagName('head')[0].appendChild(script);


function Delete(timeend, dateend) {
    console.log("sending request");
	console.log(timeend[0], timeend[1]);
	console.log(dateend);
	console.log('still sneding');
    // Extract CSRF token from cookies
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        type: "POST",
        url: "/personschedule/event-sample.html/",
        headers: {
            "X-CSRFToken": csrftoken // Include CSRF token in headers
        },
        data: {
            'day': dateend[0],
			'month': dateend[1],
			'year': dateend[2],
            'hour': timeend[0],
			'minute': timeend[1],
        },
        success: function(response) {
            // Handle the response from Django view
            console.log(response);
        },
        error: function(xhr, errmsg, err) {
            // Handle error
            console.log(xhr.status + ": " + xhr.responseText);
        }
    });
}

// Function to extract CSRF token from cookies
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Check if the cookie name matches the csrf token name
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Lots of this code was provided by codyhouse with a free use license (https://codyhouse.co/license under framework) and (heavily) edited by team

(function() {
	// initialize global variables
	var gdataend = '';
	var gdatadate = '';
	var glastdiv = '';
	var gflag = false;
	var gstring = '<!DOCTYPE html><html><head><link rel="stylesheet" href="/static/css/style.css"><script src = "/static/js/util.js"></script> <!-- util functions included in the CodyHouse framework --><script src = "/static/js/main.js"></script></head><body><div class="cd-schedule-modal__event-info"><h1>  Surgery Infohehehehaw</h1></div></body></html>';
	// Schedule Template - by CodyHouse.co
	function ScheduleTemplate( element ) {
		this.element = element;
		this.timelineItems = this.element.getElementsByClassName('cd-schedule__timeline')[0].getElementsByTagName('li');
		this.timelineStart = getScheduleTimestamp(this.timelineItems[0].textContent);
		this.timelineUnitDuration = getScheduleTimestamp(this.timelineItems[1].textContent) - getScheduleTimestamp(this.timelineItems[0].textContent);
		
		this.topInfoElement = this.element.getElementsByClassName('cd-schedule__top-info')[0];
		this.singleEvents = this.element.getElementsByClassName('cd-schedule__event');
		
		this.modal = this.element.getElementsByClassName('cd-schedule-modal')[0];
		this.modalHeader = this.element.getElementsByClassName('cd-schedule-modal__header')[0];
		this.modalHeaderBg = this.element.getElementsByClassName('cd-schedule-modal__header-bg')[0];
		this.modalBody = this.element.getElementsByClassName('cd-schedule-modal__body')[0];
		this.modalBodyBg = this.element.getElementsByClassName('cd-schedule-modal__body-bg')[0];
		this.modalClose = this.modal.getElementsByClassName('cd-schedule-modal__close')[0];
		this.modalDate = this.modal.getElementsByClassName('cd-schedule-modal__date')[0];
		this.modalEventName = this.modal.getElementsByClassName('cd-schedule-modal__name')[0];
		this.coverLayer = this.element.getElementsByClassName('cd-schedule__cover-layer')[0];

		this.modalMaxWidth = 800;
		this.modalMaxHeight = 480;

		this.animating = false;
		this.supportAnimation = Util.cssSupports('transition');

		this.initSchedule();
	};

	ScheduleTemplate.prototype.initSchedule = function() {
		this.scheduleReset();
		this.initEvents();
	};


	ScheduleTemplate.prototype.scheduleReset = function() {
		// according to the mq value, init the style of the template
		var mq = this.mq(),
			loaded = Util.hasClass(this.element, 'js-schedule-loaded'),
			modalOpen = Util.hasClass(this.modal, 'cd-schedule-modal--open');
		if( mq == 'desktop' && !loaded ) {
			Util.addClass(this.element, 'js-schedule-loaded');
			this.placeEvents();
			modalOpen && this.checkEventModal(modalOpen);
		} else if( mq == 'mobile' && loaded) {
			//in this case you are on a mobile version (first load or resize from desktop)
			Util.removeClass(this.element, 'cd-schedule--loading js-schedule-loaded');
			this.resetEventsStyle();
			modalOpen && this.checkEventModal();
		} else if( mq == 'desktop' && modalOpen ) {
			//on a mobile version with modal open - need to resize/move modal window
			this.checkEventModal(modalOpen);
			Util.removeClass(this.element, 'cd-schedule--loading');
		} else {
			Util.removeClass(this.element, 'cd-schedule--loading');
		}
	};

	ScheduleTemplate.prototype.resetEventsStyle = function() {
		// remove js style applied to the single events
		for(var i = 0; i < this.singleEvents.length; i++) {
			this.singleEvents[i].removeAttribute('style');
		}
	};

	ScheduleTemplate.prototype.placeEvents = function() {
		// on big devices - place events in the template according to their time/day
		var self = this,
			slotHeight = this.topInfoElement.offsetHeight;
		for(var i = 0; i < this.singleEvents.length; i++) {
			var anchor = this.singleEvents[i].getElementsByTagName('a')[0];
			var start = getScheduleTimestamp(anchor.getAttribute('data-start')),
				duration = getScheduleTimestamp(anchor.getAttribute('data-end')) - start;

			var eventTop = slotHeight*(start - self.timelineStart)/self.timelineUnitDuration,
				eventHeight = slotHeight*duration/self.timelineUnitDuration;

			this.singleEvents[i].setAttribute('style', 'top: '+(eventTop-1)+'px; height: '+(eventHeight +1)+'px');
		}

		Util.removeClass(this.element, 'cd-schedule--loading');
	};



	ScheduleTemplate.prototype.initEvents = function() {
		var self = this;
		console.log("here");
		for(var i = 0; i < this.singleEvents.length; i++) {
			// open modal when user selects an event
			this.singleEvents[i].addEventListener('click', function(event){
				//self.sendRequest(this.getElementsByTagName('a')[0]);
				event.preventDefault();
				if(!self.animating && !gflag){
					self.openModal(this.getElementsByTagName('a')[0]);
					gflag = true;
				}
				gflag = false;
			});
			gflag = false;
		}
		//close modal window
		this.modalClose.addEventListener('click', function(event){
			event.preventDefault();
			if( !self.animating ) self.closeModal();
		});
		this.coverLayer.addEventListener('click', function(event){
			event.preventDefault();
			if( !self.animating ) self.closeModal();
		});
	};

	ScheduleTemplate.prototype.openModal = function(target) {
		gdataend = target.getAttribute('data-end');
		gdatadate = target.getAttribute('data-date');
		$.ajax({
			type: "GET", // or "GET" depending on your requirements
			url: "/personschedule/event-sample.html/",
			data: {
				'dataend': gdataend, // Send your variable as data
				'datadate': gdatadate,
			},
			success: function(response) {
				// Handle the response from Django view
				gstring = response.string;
			},
			error: function(xhr, errmsg, err) {
				// Handle error (never happens :))
				console.log(xhr.status + ": " + xhr.responseText); // Log any errors
			}
		});
		var self = this;
		if (!gflag){
			gflag = true;
			self.openModal(target);
		}
		gflag = false;
		
		//update event name and time
		var mq = self.mq();
		this.animating = true;	
		this.modalEventName.textContent = target.getElementsByTagName('em')[0].textContent;
		this.modalDate.textContent = target.getAttribute('data-start')+' - '+target.getAttribute('data-end');
		this.modal.setAttribute('data-event', target.getAttribute('data-event'));
		console.log(this.modalDate);
		//this.modalBody.getElementById('label').innerHTML = 'success!';
		//update event content
		this.loadEventContent(target.getAttribute('data-content'));
		
		
		
		Util.addClass(this.modal, 'cd-schedule-modal--open');
		
		setTimeout(function(){
			//fixes a flash when an event is selected - desktop version only
			Util.addClass(target.closest('li'), 'cd-schedule__event--selected');
		}, 10);


		

		if( mq == 'mobile' ) {
			self.modal.addEventListener('transitionend', function cb(){
				self.animating = false;
				self.modal.removeEventListener('transitionend', cb);
			});
		} else {
			var eventPosition = target.getBoundingClientRect(),
				eventTop = eventPosition.top,
				eventLeft = eventPosition.left,
				eventHeight = target.offsetHeight,
				eventWidth = target.offsetWidth;

			var windowWidth = window.innerWidth,
				windowHeight = window.innerHeight;

			var modalWidth = ( windowWidth*.8 > self.modalMaxWidth ) ? self.modalMaxWidth : windowWidth*.8,
				modalHeight = ( windowHeight*.8 > self.modalMaxHeight ) ? self.modalMaxHeight : windowHeight*.8;

			var modalTranslateX = parseInt((windowWidth - modalWidth)/2 - eventLeft),
				modalTranslateY = parseInt((windowHeight - modalHeight)/2 - eventTop);
			
			var HeaderBgScaleY = modalHeight/eventHeight,
				BodyBgScaleX = (modalWidth - eventWidth);

			//change modal height/width and translate it
			self.modal.setAttribute('style', 'top:'+eventTop+'px;left:'+eventLeft+'px;height:'+modalHeight+'px;width:'+modalWidth+'px;transform: translateY('+modalTranslateY+'px) translateX('+modalTranslateX+'px)');
			//set modalHeader width
			self.modalHeader.setAttribute('style', 'width:'+eventWidth+'px');
			//set modalBody left margin
			self.modalBody.setAttribute('style', 'margin-left:'+eventWidth+'px');
			//change modalBodyBg height/width ans scale it
			self.modalBodyBg.setAttribute('style', 'height:'+eventHeight+'px; width: 1px; transform: scaleY('+HeaderBgScaleY+') scaleX('+BodyBgScaleX+')');
			//change modal modalHeaderBg height/width and scale it
			self.modalHeaderBg.setAttribute('style', 'height: '+eventHeight+'px; width: '+eventWidth+'px; transform: scaleY('+HeaderBgScaleY+')');
			
			self.modalHeaderBg.addEventListener('transitionend', function cb(){
				//wait for the  end of the modalHeaderBg transformation and show the modal content
				self.animating = false;
				Util.addClass(self.modal, 'cd-schedule-modal--animation-completed');
				self.modalHeaderBg.removeEventListener('transitionend', cb);
			});
		}
		//if browser do not support transitions -> no need to wait for the end of it
		this.animationFallback();
		
	};

	ScheduleTemplate.prototype.closeModal = function() {
		var self = this;
		var mq = self.mq();

		var item = self.element.getElementsByClassName('cd-schedule__event--selected')[0],
			target = item.getElementsByTagName('a')[0];

		this.animating = true;

		if( mq == 'mobile' ) {
			Util.removeClass(this.modal, 'cd-schedule-modal--open');
			self.modal.addEventListener('transitionend', function cb(){
				Util.removeClass(self.modal, 'cd-schedule-modal--content-loaded');
				Util.removeClass(item, 'cd-schedule__event--selected');
				self.animating = false;
				self.modal.removeEventListener('transitionend', cb);
			});
		} else {
			var eventPosition = target.getBoundingClientRect(),
				eventTop = eventPosition.top,
				eventLeft = eventPosition.left,
				eventHeight = target.offsetHeight,
				eventWidth = target.offsetWidth;

			var modalStyle = window.getComputedStyle(self.modal),
				modalTop = Number(modalStyle.getPropertyValue('top').replace('px', '')),
				modalLeft = Number(modalStyle.getPropertyValue('left').replace('px', ''));

			var modalTranslateX = eventLeft - modalLeft,
				modalTranslateY = eventTop - modalTop;

			Util.removeClass(this.modal, 'cd-schedule-modal--open cd-schedule-modal--animation-completed');

			//change modal width/height and translate it
			self.modal.style.width = eventWidth+'px';self.modal.style.height = eventHeight+'px';self.modal.style.transform = 'translateX('+modalTranslateX+'px) translateY('+modalTranslateY+'px)';
			//scale down modalBodyBg element
			self.modalBodyBg.style.transform = 'scaleX(0) scaleY(1)';
			//scale down modalHeaderBg element
			// self.modalHeaderBg.setAttribute('style', 'transform: scaleY(1)');
			self.modalHeaderBg.style.transform = 'scaleY(1)';

			self.modalHeaderBg.addEventListener('transitionend', function cb(){
				//wait for the  end of the modalHeaderBg transformation and reset modal style
				Util.addClass(self.modal, 'cd-schedule-modal--no-transition');
				setTimeout(function(){
					self.modal.removeAttribute('style');
					self.modalBody.removeAttribute('style');
					self.modalHeader.removeAttribute('style');
					self.modalHeaderBg.removeAttribute('style');
					self.modalBodyBg.removeAttribute('style');
				}, 10);
				setTimeout(function(){
					Util.removeClass(self.modal, 'cd-schedule-modal--no-transition');
				}, 20);
				self.animating = false;
				Util.removeClass(self.modal, 'cd-schedule-modal--content-loaded');
				Util.removeClass(item, 'cd-schedule__event--selected');
				self.modalHeaderBg.removeEventListener('transitionend', cb);
			});
		}

		//if browser do not support transitions -> no need to wait for the end of it
		this.animationFallback();
	};

	ScheduleTemplate.prototype.checkEventModal = function(modalOpen) {
		// this function is used on resize to reset events/modal style
		this.animating = true;
		var self = this;
		var mq = this.mq();
		if( mq == 'mobile' ) {
			//reset modal style on mobile
			self.modal.removeAttribute('style');
			self.modalBody.removeAttribute('style');
			self.modalHeader.removeAttribute('style');
			self.modalHeaderBg.removeAttribute('style');
			self.modalBodyBg.removeAttribute('style');
			Util.removeClass(self.modal, 'cd-schedule-modal--no-transition');
			self.animating = false;	
		} else if( mq == 'desktop' && modalOpen) {
			Util.addClass(self.modal, 'cd-schedule-modal--no-transition cd-schedule-modal--animation-completed');
			var item = self.element.getElementsByClassName('cd-schedule__event--selected')[0],
				target = item.getElementsByTagName('a')[0];

			var eventPosition = target.getBoundingClientRect(),
				eventTop = eventPosition.top,
				eventLeft = eventPosition.left,
				eventHeight = target.offsetHeight,
				eventWidth = target.offsetWidth;

			var windowWidth = window.innerWidth,
				windowHeight = window.innerHeight;

			var modalWidth = ( windowWidth*.8 > self.modalMaxWidth ) ? self.modalMaxWidth : windowWidth*.8,
				modalHeight = ( windowHeight*.8 > self.modalMaxHeight ) ? self.modalMaxHeight : windowHeight*.8;

			var HeaderBgScaleY = modalHeight/eventHeight,
				BodyBgScaleX = (modalWidth - eventWidth);


			setTimeout(function(){
				self.modal.setAttribute('style', 'top:'+(windowHeight/2 - modalHeight/2)+'px;left:'+(windowWidth/2 - modalWidth/2)+'px;height:'+modalHeight+'px;width:'+modalWidth+'px;transform: translateY(0) translateX(0)');
				//change modal modalBodyBg height/width
				self.modalBodyBg.style.height = modalHeight+'px';self.modalBodyBg.style.transform = 'scaleY(1) scaleX('+BodyBgScaleX+')';self.modalBodyBg.style.width = '1px';
				//set modalHeader width
				self.modalHeader.setAttribute('style', 'width:'+eventWidth+'px');
				//set modalBody left margin
				self.modalBody.setAttribute('style', 'margin-left:'+eventWidth+'px');
				//change modal modalHeaderBg height/width and scale it
				self.modalHeaderBg.setAttribute('style', 'height: '+eventHeight+'px;width:'+eventWidth+'px; transform:scaleY('+HeaderBgScaleY+');');
			}, 10);

			setTimeout(function(){
				Util.removeClass(self.modal, 'cd-schedule-modal--no-transition');
				self.animating = false;	
			}, 20);

		}
	};

	ScheduleTemplate.prototype.loadEventContent = function(content) {
		var self = this;
		var httpRequest = new XMLHttpRequest();
		httpRequest.onreadystatechange = function() {
			if (httpRequest.readyState === XMLHttpRequest.DONE) {
				if (httpRequest.status === 200) {
					var eventInfoElement = self.modal.querySelector('.cd-schedule-modal__event-info');
					if (eventInfoElement) {
						eventInfoElement.innerHTML = gstring;
						Util.addClass(self.modal, 'cd-schedule-modal--content-loaded');
					} else {
						console.error('Element with class "cd-schedule-modal__event-info" not found in modal.');
					}
				} else {
					console.error('Error:', httpRequest.status); // Log error status
				}
			}
		};
		// Construct the AJAX request URL with the info parameter
		var url = "/personschedule?dataend=" + encodeURIComponent(gdataend) + "&datadate=" + encodeURIComponent(gdatadate);
    	httpRequest.open('GET', url);
    	httpRequest.send();
	};

	ScheduleTemplate.prototype.getEventContent = function(string) {
		// reset the loaded event content so that it can be inserted in the modal
		var div = document.createElement('div');
		div.innerHTML = string.trim();
		console.log(div.getElementsByClassName('cd-schedule-modal__event-info')[0]);
		console.log(glastdiv)
		if (div.getElementsByClassName('cd-schedule-modal__event-info')[0] == true){
			glastdiv = div.getElementsByClassName('cd-schedule-modal__event-info')[0];
		}
		return glastdiv;
	};

	ScheduleTemplate.prototype.animationFallback = function() {
		if( !this.supportAnimation ) { // fallback for browsers not supporting transitions
			var event = new CustomEvent('transitionend');
			self.modal.dispatchEvent(event);
			self.modalHeaderBg.dispatchEvent(event);
		}
	};

	ScheduleTemplate.prototype.mq = function(){
		//get MQ value ('desktop' or 'mobile') 
		var self = this;
		return window.getComputedStyle(this.element, '::before').getPropertyValue('content').replace(/'|"/g, "");
	};

	function getScheduleTimestamp(time) {
		//accepts hh:mm format - convert hh:mm to timestamp
		time = time.replace(/ /g,'');
		var timeArray = time.split(':');
		var timeStamp = parseInt(timeArray[0])*60 + parseInt(timeArray[1]);
		return timeStamp;
	};

	var scheduleTemplate = document.getElementsByClassName('js-cd-schedule'),	
		scheduleTemplateArray = [],
		resizing = false;
	if( scheduleTemplate.length > 0 ) { // init ScheduleTemplate objects
		for( var i = 0; i < scheduleTemplate.length; i++) {
			(function(i){
				scheduleTemplateArray.push(new ScheduleTemplate(scheduleTemplate[i]));
			})(i);
		}

		window.addEventListener('resize', function(event) { 
			// on resize - update events position and modal position (if open)
			if( !resizing ) {
				resizing = true;
				(!window.requestAnimationFrame) ? setTimeout(checkResize, 250) : window.requestAnimationFrame(checkResize);
			}
		});

		window.addEventListener('keyup', function(event){
			// close event modal when pressing escape key
			if( event.keyCode && event.keyCode == 27 || event.key && event.key.toLowerCase() == 'escape' ) {
				for(var i = 0; i < scheduleTemplateArray.length; i++) {
					scheduleTemplateArray[i].closeModal();
				}
			}
		});

		function checkResize(){
			for(var i = 0; i < scheduleTemplateArray.length; i++) {
				scheduleTemplateArray[i].scheduleReset();
			}
			resizing = false;
		};
	}
}());
