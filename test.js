function cakes(recipe, available){
    for (let i = 0; i < recipe.length; i++){
        if (!available.hasOwnProperty(recipe[i])){
            return 0;
        }
        else if (recipe[i] == available[i]){
            
        }
    }
}






let recipe = {flour: 500, sugar: 200, eggs: 1};
let available = {flour: 1200, sugar: 1200, eggs: 5, milk: 200};

