## Problem 1

### Background: 

The TST cruise application receives pricing and rate information from a third party data provider. We make two calls to this provider to receive a list of rates and a list of cabin prices. We can use this data to solve several problems for our customers. The problem we’ll be focusing on for this exercise will be finding the best price for a particular rate group.

**Cabin Price:** The price for a specific cabin on a specific cruise. All cabin prices will have a single rate attached.
**Rate:** A rate is a way to group related prices together. A rate is defined by its Rate Code and which Rate Group it belongs to. For example. (MilAB, Military) and (Sen123, Senior)
**Rate Group:** Specific rates are grouped into a related rate group. There is a one-to-many relationship between rate groups and rates (A rate group is made up of many rates, but a rate can only belong to a single rate group) Some examples of rate groups are: Standard, Military, Senior, and Promotion.


1. Write a function that will take a list of rates and a list of prices and returns the best price for each rate group. We’ve supplied the function and case class definitions below for you to use.

```python3
# given the following function
def get_best_group_prices(
    rates: List[Rate], 
    prices: List[CabinPrice]
) -> List[BestGroupPrice] :
```
2. On startup, your program should run the following sample data through your function and output the sequence of BestGroupPrices.

## Problem 2

**Background**: Cruise bookings can have one or more Promotions applied to them. But sometimes a Promotion cannot be combined with another Promotion. Our application has to find out all possible Promotion Combinations that can be applied together.

1. Implement a function to find all PromotionCombos with maximum number of combinable promotions in each. The function and case class definitions are supplied below to get you started.
```python
def all_combinable_promotions(
    all_promotions: List[Promotion],
) -> List[PromotionCombo]:
```
2. Implement a function to find all PromotionCombos for a given Promotion from given list of Promotions. The function definition is provided. 
```python
def combinable_promotions(
    promotion_code: str,
    all_promotions: List[PromotionCombo],
) -> List[PromotionCombo]:
```
3. On startup your program should run through the following sample data and output the sequence of PromotionCombos.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.10 or higher
- pip (Python package installer)

### Installing

A step by step series of examples that tell you how to get a development environment running:

1. **Clone the repository**

```bash
git clone https://github.com/amnotme/TST-Project.git
cd TST-Project/PythonSolution
```
2. **Set up a virtual environment**

```bash
# Mac
python3 -m venv env
source env/bin/activate

# Win
python -m venv env
.\env\Scripts\activate
```

3. **Install required packages**

```bash
pip install -r requirements.txt
```
4. **Running Solutions**

```bash
# all
python main.py
```

5. **Running Tests**
```bash
# You can run all of the at once when at root TST-Project/PythonSolution
pytest
# individually
pytest tests/test_problem_one.py
pytest tests/test_problem_two.py


```