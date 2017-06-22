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

  self.activity = ko.observable();

  self.featuresArray = ko.observableArray([]);
  self.featureCols = ['Id', 'Title', 'Description', 'Client Id', 'Client Name', 'Priority', 'Target Date', 'Product Area Id', 'Product Area Name', 'Submitter Id', 'Submitter Name'];

  self.newFeatureId = ko.observable();
  self.newFeatureTitle = ko.observable();
  self.newFeatureDescription = ko.observable();
  self.newFeatureClient_name = ko.observable();
  self.newFeaturePriority = ko.observable();
  self.newFeatureTargetDate = ko.observable();
  self.newFeatureProductArea_name = ko.observable();
  self.newFeatureSubmitterName = ko.observable();

  self.clientsArray = ko.observableArray([]);
  self.clientCols = ['Id', 'Client Name'];
  self.newClientId = ko.observable();
  self.newClientName = ko.observable();

  self.usersArray = ko.observableArray([]);
  self.userCols = ['Id', 'User Name'];
  self.newUserId = ko.observable();
  self.newUserName = ko.observable();

  self.productAreasArray = ko.observableArray([]);
  self.productAreaCols = ['Id', 'Product Area Name'];
  self.newProductAreaId = ko.observable();
  self.newProductAreaName = ko.observable();

  self.goToNav = function(nav) {
    self.chosenNavId(nav);
    self.clearObs();
  };

  self.clearObs = function() {
    self.newFeatureId('');
    self.newFeatureTitle('');
    self.newFeatureDescription('');
    self.newFeatureClient_name('');
    self.newFeaturePriority('');
    self.newFeatureTargetDate('');
    self.newFeatureProductArea_name('');
    self.newFeatureSubmitterName('');
    self.newClientId('');
    self.newClientName('');
    self.newUserId('');
    self.newUserName('');
    self.newProductAreaId('');
    self.newProductAreaName('');
  }

  self.showAddFeature = function() {
    self.chosenNavId('addFeature');
    self.activity('Add');
  };

  self.showEditFeature = function(feature) {
    self.newFeatureId(feature.id());
    self.newFeatureTitle(feature.title());
    self.newFeatureDescription(feature.description());
    self.newFeatureClient_name(feature.client_name());
    self.newFeaturePriority(feature.priority());
    self.newFeatureTargetDate(feature.targetDate());
    self.newFeatureProductArea_name(feature.productArea_name());
    self.newFeatureSubmitterName(feature.submitter_name());
    self.chosenNavId('editFeature');
    self.activity('Edit');

  };

  self.showAddClient = function() {
    self.chosenNavId('addClient');
    self.activity('Add');
  };

  self.showEditClient = function(client) {
    self.newClientId(client.id());
    self.newClientName(client.client_name());
    self.chosenNavId('editClient');
    self.activity('Edit');

  };

  self.showAddUser = function() {
    self.chosenNavId('addUser');
    self.activity('Add');
  };

  self.showEditUser = function(user) {
    self.newUserId(user.id());
    self.newUserName(user.user_name());
    self.chosenNavId('editUser');
    self.activity('Edit');

  };

  self.showAddProductArea = function() {
    self.chosenNavId('addProductArea');
    self.activity('Add');
  };
  
  self.showEditProductArea = function(productArea) {
    console.log(productArea);
    self.newProductAreaId(productArea.id());
    self.newProductAreaName(productArea.productArea_name());
    self.chosenNavId('editProductArea');
    self.activity('Edit');

  };

  self.featureMod = function() {
    if (this.newFeatureId() !== '') {
      modFeature = new Feature({
        id: this.newFeatureId(),
        title: this.newFeatureTitle(),
        description: this.newFeatureDescription(),
        client_name: this.newFeatureClient_name(),
        priority: this.newFeaturePriority(),
        targetDate: this.newFeatureTargetDate(),
        productArea_name: this.newFeatureProductArea_name(),
        submitter_name: this.newFeatureSubmitterName()
      });
      //     self.featuresArray.push(newFeature);
      $.ajax("/edit_feature", {
        data: ko.toJSON(modFeature),
        type: "post",
        contentType: "application/json",
        success: function(data) {
          var mappedFeatures = $.map(data.features, function(item) {
            return new Feature(item)
          });
          self.featuresArray(mappedFeatures);
        }
      });
    } else {
      newFeature = new Feature({
        title: this.newFeatureTitle(),
        description: this.newFeatureDescription(),
        client_name: this.newFeatureClient_name(),
        priority: this.newFeaturePriority(),
        targetDate: this.newFeatureTargetDate(),
        productArea_name: this.newFeatureProductArea_name(),
        submitter_name: this.newFeatureSubmitterName()
      });
      //     self.featuresArray.push(newFeature);
      $.ajax("/add_feature", {
        data: ko.toJSON(newFeature),
        type: "post",
        contentType: "application/json",
        success: function(data) {
          var mappedFeatures = $.map(data.features, function(item) {
            return new Feature(item)
          });
          self.featuresArray(mappedFeatures);
        }
      });
    }

    self.clearObs();
    self.chosenNavId('Features');
  };

  self.clientMod = function() {
    if (this.newClientId() !== '') {
      modClient = new Client({
        id: this.newClientId(),
        client_name: this.newClientName()
      });
      console.log(ko.toJSON(modClient));

      $.ajax("/edit_client", {
        data: ko.toJSON(modClient),
        type: "post",
        contentType: "application/json",
        success: function(data) {
          var mappedClients = $.map(data.clients, function(item) {
            return new Client(item)
          });
          self.clientsArray(mappedClients);

        }
      });
    } else {
      newClient = new Client({
        client_name: this.newClientName()
      });
      //     self.clientsArray.push(newClient);
      $.ajax("/add_client", {
        data: ko.toJSON(newClient),
        type: "post",
        contentType: "application/json",
        success: function(data) {
          var mappedClients = $.map(data.clients, function(item) {
            return new Client(item)
          });
          self.clientsArray(mappedClients);

        }
      });
    }
    self.clearObs();
    self.chosenNavId('Clients');
  };

  self.modUser = function() {
    if (this.newUserId() !== '') {
      modUser = new User({
        id: this.newUserId(),
        user_name: this.newUserName()
      });
      //     self.usersArray.push(newUser);
      $.ajax("/edit_user", {
        data: ko.toJSON(modUser),
        type: "post",
        contentType: "application/json",
        success: function(data) {
          var mappedUsers = $.map(data.users, function(item) {
            return new User(item)
          });
          self.usersArray(mappedUsers);
        }
      });
    } else {
      newUser = new User({
        user_name: this.newUserName()
      });
      //     self.usersArray.push(newUser);
      $.ajax("/add_user", {
        data: ko.toJSON(newUser),
        type: "post",
        contentType: "application/json",
        success: function(data) {
          var mappedUsers = $.map(data.users, function(item) {
            return new User(item)
          });
          self.usersArray(mappedUsers);
        }
      });
    }

    self.clearObs();
    self.chosenNavId('Users');
  };

  self.modProductArea = function() {
    if (self.newProductAreaId() !== '') {
      modProductArea = new ProductArea({
        id: this.newProductAreaId(),
        productArea_name: this.newProductAreaName()
      });
      //     self.productAreasArray.push(newProductArea);
      $.ajax("/edit_product_area", {
        data: ko.toJSON(modProductArea),
        type: "post",
        contentType: "application/json",
        success: function(data) {
          var mappedProductAreas = $.map(data.product_areas, function(item) {
            return new ProductArea(item)
          });
          self.productAreasArray(mappedProductAreas);
        }
      });
    }
    else {
      newProductArea = new ProductArea({
      productArea_name: this.newProductAreaName()
    });
    //     self.productAreasArray.push(newProductArea);
    $.ajax("/add_product_area", {
      data: ko.toJSON(newProductArea),
      type: "post",
      contentType: "application/json",
      success: function(data) {
        var mappedProductAreas = $.map(data.product_areas, function(item) {
          return new ProductArea(item)
        });
        self.productAreasArray(mappedProductAreas);
      }
    });
    }
    
    self.clearObs();
    self.chosenNavId('Product Areas');
  };

  self.getFeatures = function() {
    $.getJSON("/features", function(data) {
      var mappedFeatures = $.map(data.features, function(item) {
        return new Feature(item)
      });
      self.featuresArray(mappedFeatures);
    });
  };

  self.getClients = function() {
    $.getJSON("/clients", function(data) {
      var mappedClients = $.map(data.clients, function(item) {
        return new Client(item)
      });
      self.clientsArray(mappedClients);
    });
  };

  self.getUsers = function() {
    $.getJSON("/users", function(data) {
      var mappedUsers = $.map(data.users, function(item) {
        return new User(item)
      });
      self.usersArray(mappedUsers);
    });
  };

  self.getProductAreas = function() {
    $.getJSON("/product_areas", function(data) {
      var mappedProductAreas = $.map(data.product_areas, function(item) {
        return new ProductArea(item)
      });
      self.productAreasArray(mappedProductAreas);
    });
  };

  self.getFeatures();
  self.getClients();
  self.getUsers();
  self.getProductAreas();

  self.goToNav('Features');
};

ko.applyBindings(new FeatureModel());