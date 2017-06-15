function Feature(data) {
  this.id = ko.observable(data.id);
  this.title = ko.observable(data.title);
  this.description = ko.observable(data.description);
  this.client_id = ko.observable(data.client_id);
  this.client_name = ko.observable(data.client_name);
  this.priority = ko.observable(data.priority);
  this.targetDate = ko.observable(data.targetDate);
  this.productArea_id = ko.observable(data.productArea_id);
  this.productArea_name = ko.observable(data.productArea_name);
  this.submitter_id = ko.observable(data.submitter_id);
  this.submitter_name = ko.observable(data.submitter_name);
}

function Client(data) {
  this.id = ko.observable(data.id);
  this.client_name = ko.observable(data.client_name);
}

function User(data) {
  this.id = ko.observable(data.id);
  this.user_name = ko.observable(data.user_name);
}

function ProductArea(data) {
  this.id = ko.observable(data.id);
  this.productArea_name = ko.observable(data.productArea_name);
}

var FeatureModel = function() {
  var self = this;
  self.navs = ['Features', 'Clients', 'Users', 'Product Areas'];
  self.chosenNavId = ko.observable();

  self.featuresArray = ko.observableArray([]);
  self.featureCols = ['Id', 'Title', 'Description', 'Client Id', 'Client Name', 'Priority', 'Target Date', 'Product Area Id', 'Product Area Name', 'Submitter Id', 'Submitter Name'];
  self.newFeatureTitle = ko.observable();
  self.newFeatureDescription = ko.observable();
  self.newFeatureClient_name = ko.observable();
  self.newFeaturePriority = ko.observable();
  self.newFeatureTargetDate = ko.observable();
  self.newFeatureProductArea_name = ko.observable();
  self.newFeatureSubmitterName = ko.observable();

  self.clientsArray = ko.observableArray([]);
  self.clientCols = ['Id', 'Client Name'];
  self.newClientName = ko.observable();

  self.usersArray = ko.observableArray([]);
  self.userCols = ['Id', 'User Name'];
  self.newUserName = ko.observable();

  self.productAreasArray = ko.observableArray([]);
  self.productAreaCols = ['Id', 'User Name'];
  self.newProductAreaName = ko.observable();

  self.goToNav = function(nav) {
    self.chosenNavId(nav);
  };

  self.addFeature = function() {
    newFeature = new Feature({
      title: this.newFeatureTitle(),
      description: this.newFeatureDescription(),
      client_name: this.newFeatureClient_name(),
      priority: this.newFeaturePriority(),
      targetDate: this.newFeatureTargetDate(),
      productArea_name: this.newFeatureProductArea_name(),
      submitter_name: this.newFeatureSubmitterName()
    });
    self.featuresArray.push(newFeature);
    $.ajax("/add_feature", {
      data: ko.toJSON(newFeature),
      type: "post",
      contentType: "application/json"
    });
    self.newFeatureTitle("");
    self.newFeatureDescription("");
    self.newFeatureClient_name("");
    self.newFeaturePriority("");
    self.newFeatureTargetDate("");
    self.newFeatureProductArea_name("");
    self.newFeatureSubmitterName("");
  };
  
  self.addClient = function() {
    newClient = new Client({
      client_name: this.newClientName()
    });
    self.clientsArray.push(newClient);
    $.ajax("/add_client", {
      data: ko.toJSON(newClient),
      type: "post",
      contentType: "application/json"
    });
    self.newClientName("");
  };

  $.getJSON("/features", function(data) {
    var mappedFeatures = $.map(data.features, function(item) {
      return new Feature(item)
    });
    self.featuresArray(mappedFeatures);
  });
  $.getJSON("/clients", function(data) {
    var mappedClients = $.map(data.clients, function(item) {
      return new Client(item)
    });
    self.clientsArray(mappedClients);
  });
  $.getJSON("/users", function(data) {
    var mappedUsers = $.map(data.users, function(item) {
      return new User(item)
    });
    self.usersArray(mappedUsers);
  });
  $.getJSON("/product_areas", function(data) {
    var mappedProductAreas = $.map(data.product_areas, function(item) {
      return new ProductArea(item)
    });
    self.productAreasArray(mappedProductAreas);
  });
  self.goToNav('Features');
};

ko.applyBindings(new FeatureModel());