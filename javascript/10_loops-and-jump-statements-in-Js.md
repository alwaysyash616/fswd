### Prerequisites
```mermaid
flowchart TD
    JS["JavaScript"] --> P["Primitive"]
    JS --> NP["Non-primitive"]

    P --> S["String"]
    P --> N["Number"]
    P --> B["Boolean"]
    P --> NU["Null"]
    P --> U["Undefined"]
    P --> SY["Symbol"]
    P --> BI["BigInt"]

    NP --> O["Object"]
    NP --> A["Array"]
    NP --> F["Function"]

    F -.-> |technically| O
    A -.-> |technically| O
```
### How to make object in JS?
```js
let x = {
    name: "Yash",
    age: 24,
    salary: '$180,000'
}
console.log(x)
```
### Access individual properties/values
```js
// ---------I---------
console.log(x.name);
console.log(x.age);
// ---II (more powerful, better way)---
console.log(x['name']);
console.log(x['age']);
```
### Why `typeof [2,4,5]` is an object?
> what if keys? are numbers? - 0, 1, 2 ...  
> Then,  
> console.log(obj.0) `❌`  
> console.log(obj.1) `❌`  
> `console.log(obj['0'])` `✅`(like this will work)  
> but  
> `console.log(obj[0])`  `✅` is more convenient  

# Loops and Jump statements
```mermaid
flowchart TD

    CS["JavaScript<br/>Control Statements"]
    
    CS --> DC["Decision Control<br/>Statements"]
    CS --> IC["Iterative Control<br/>Statements"]
    CS --> JS["Jump Statements"]

    DC -.-> Y["Yesterday"]
    IC -.-> T["Today"]
    JS -.-> T

    IC --> L["Loops"]

    L --> W["while"]
    L --> DW["do-while"]
    L --> F["for"]
    L --> FI["for-in"]
    L --> FO["for-of"]

    W --> WC["Like C"]
    WC --> WP["Same behavior in<br/>Python, C++, Java & JavaScript"]

    DW --> DWC["Like C"]
    DWC --> NP["Not in Python"]

    F --> FC["Little different<br/>from Python"]
    FC --> CLike["Mostly like<br/>C, C++ & Java"]

    FI --> FID["JavaScript<br/>for-in"]

    FO --> FOP["Behavior like<br/>Python's for loop"]

    style CS fill:none,stroke-width:2px
    style IC fill:none,stroke-width:2px
    style L fill:none,stroke-width:2px
```

### `for-in` & `for-of` Loops

> `while`, `do-while` & `for` in JavaScript are like C; now we see `for-in` & `for-of`.

#### `for-in` Loop

```js
for (let V in object) {
    // code
}
```

- `V` contains **property names (keys)**, one by one.
- For an object, use `object[V]` to access the corresponding value.

```js
const p1 = {
    name: "Rahul",
    age: 22,
    city: "Bhopal",
    f1: function () {
        console.log("Hello");
    }
};

for (let prop in p1) {
    console.log(prop, p1[prop]);
}
```

`p1.prop` → `undefined` because there is no property named `prop`.

#### `for-of` Loop

```js
for (let V of iterable) {
    // code
}
```

- `V` contains **values**, one by one.
- Arrays are iterable.

```js
let a = [11, 22, 33, 44];

for (let V of a) {
    console.log(V);
}
```

Output:
```text
11
22
33
44
```

**Remember:**

- `for-in` → **keys / property names**
- `for-of` → **values**

#### Iterables & Objects

- **All iterables are objects.**
- Arrays, functions & objects are objects.
- Therefore, an **array** can be used with both `for-in` and `for-of`.
> Array is special object in which _property names_ **(keys)** are 0,1,2,3...  
> `obj[0]` `✅`_(more convenient)_  
> but  
> `obj['0']` `✅`_(will work)_  
> _in fact_
> _it is the actual way to access object individual elements, by writing keys in quotation in square brackets_

```js
let a = [11, 22, 33, 44];

for (let V in a) {
    console.log(V, a[V]);
}
```

`for-in` → `V` gets the **index (key)** → `0, 1, 2, 3`

```js
for (let V of a) {
    console.log(V);
}
```

`for-of` → `V` gets the **value** → `11, 22, 33, 44`

### Jump Statements

- `break` → break exits the nearest enclosing loop or switch.
- `continue` → skips current iteration and moves to the next one.
- `return` → used inside a function to return a value & exit the function.