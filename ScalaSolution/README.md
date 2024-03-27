## Problem 1

### Background: 

The TST cruise application receives pricing and rate information from a third party data provider. We make two calls to this provider to receive a list of rates and a list of cabin prices. We can use this data to solve several problems for our customers. The problem we’ll be focusing on for this exercise will be finding the best price for a particular rate group.

**Cabin Price:** The price for a specific cabin on a specific cruise. All cabin prices will have a single rate attached.
**Rate:** A rate is a way to group related prices together. A rate is defined by its Rate Code and which Rate Group it belongs to. For example. (MilAB, Military) and (Sen123, Senior)
**Rate Group:** Specific rates are grouped into a related rate group. There is a one-to-many relationship between rate groups and rates (A rate group is made up of many rates, but a rate can only belong to a single rate group) Some examples of rate groups are: Standard, Military, Senior, and Promotion.


1. Write a function that will take a list of rates and a list of prices and returns the best price for each rate group. We’ve supplied the function and case class definitions below for you to use.

```scala 3
def getBestGroupPrices(rates: Seq[Rate], prices: Seq[CabinPrice]): Seq[BestGroupPrice] = ???
```
2. On startup, your program should run the following sample data through your function and output the sequence of BestGroupPrices.

## Problem 2

**Background**: Cruise bookings can have one or more Promotions applied to them. But sometimes a Promotion cannot be combined with another Promotion. Our application has to find out all possible Promotion Combinations that can be applied together.

1. Implement a function to find all PromotionCombos with maximum number of combinable promotions in each. The function and case class definitions are supplied below to get you started.
```scala 3
def allCombinablePromotions(allPromotions: Seq[Promotion]): Seq[PromotionCombo] = ???

```
2. Implement a function to find all PromotionCombos for a given Promotion from given list of Promotions. The function definition is provided. 
```scala 3
def combinablePromotions(promotionCode: String, allPromotions: Seq[Promotion]): Seq[PromotionCombo] =
```
3. On startup your program should run through the following sample data and output the sequence of PromotionCombos.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before starting, ensure you have the following installed:
- Scala (and sbt, the Scala build tool)

1. **Clone Repository**

```bash
git clone https://github.com/amnotme/TST-Project.git
cd TST-Project/ScalaSolution
```
2. **Compile and build the project**
Navigate to the root directory of the Scala solution and use sbt:

```bash
sbt compile
```

3. **Running Solutions**

Execute the main class using sbt:

```bash
sbt run
```
4. **Running Tests**

```bash
sbt test
```
This will run all the tests included in the src/test/scala directory, ensuring your solutions meet the outlined requirements.