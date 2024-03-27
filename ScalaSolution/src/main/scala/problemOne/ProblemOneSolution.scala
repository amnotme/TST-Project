package problemOne

import Data.getInputRates
import Data.getInputCabinPrices
import problemOne.ProblemOneSolution.getBestGroupPrices

object ProblemOneSolution {
  def getBestGroupPrices(rates: Seq[Rate], prices: Seq[CabinPrice]): Seq[BestGroupPrice] = {
    // 1. Create a map from rateCode to rateGroup for easy lookup
    // 2. Group prices by rateGroup using the map created above
    // 3. Find the best price for each rate group
    // 3a. Uses pattern matching to group by cabin code and consequently the lowest price for a particular cabin type.

    if (rates.isEmpty || prices.isEmpty) then return Seq()

    val rateGroupMap = rates.map(rate => rate.rateCode -> rate.rateGroup).toMap
    val groupPrices = prices.groupBy(price => rateGroupMap(price.rateCode))

    groupPrices.flatMap {
      case (group, prices) => prices.groupBy(_.cabinCode).map {
        case (cabin, cabinPrices) =>
          val bestPrice = cabinPrices.minBy(_.price)
          BestGroupPrice(cabin, bestPrice.rateCode, bestPrice.price, group)
      }
    }.toSeq
  }
}


object RunProblemOne {

  def problemOneRun: Unit =
    val result = getBestGroupPrices(
      rates = getInputRates,
      prices = getInputCabinPrices
    )

    for {
      res <- result
    } yield println(res)
}
