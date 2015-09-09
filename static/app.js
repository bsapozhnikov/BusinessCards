var App = new Marionette.Application();

App.addRegions({
    cards: "#cards"
});

App.on('start',function(){
    var c = new Cards();
    var cardsView = new App.CardsView({collection:c});
    App.cards.show(cardsView);
});

var Card = Backbone.Model.extend({
    urlRoot: '/cards'
});
var Cards = Backbone.Collection.extend({
    model: Card,
    url: '/cards',
    initialize: function(){
	this.fetch(null,function(d){
	    this.render();
	});
    }
});

App.CardView = Marionette.ItemView.extend({
    template: "#card-template",
    tagName: "li",
    className: "card",
    events: {
	'click #delete': function(){
	    this.model.destroy();
	}
    }
});

App.CardsView = Marionette.CompositeView.extend({
    template : "#cards-template",
    childView: App.CardView,
    childViewContainer: "ul",
    events: {
	'click #add-new-card': function(){
	    var n = $('#new-card-name').val();
	    var c = $('#new-card-company').val();
	    if (n.length + c.length > 0){
		var card = new Card({name: n, company: c});
		this.collection.add(card);
		card.save();
		$('#new-card-name').val('');
		$('#new-card-company').val('');
	    }
	}
    }
});

App.start();
