// i used typescript for this because its my main language of choice
interface Person {
    name: string;
}

interface HashTable<T> {
    [key: string]: T;
}

// init the hash table
var person: HashTable<Person> = {};

person["John"] = { name: "John" };

console.log(person["John"].name);