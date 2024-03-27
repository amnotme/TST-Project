package problemOne

object Data {
  def getInputRates: Seq[Rate] =
    val allRates = Seq(
      Rate("M1", "Military"),
      Rate("M2", "Military"),
      Rate("S1", "Senior"),
      Rate("S2", "Senior"),
    )
    allRates

  def getInputCabinPrices: Seq[CabinPrice] =
    val allCabinPrices = Seq(
      CabinPrice("CA", "M1", 200.00),
      CabinPrice("CA", "M2", 250.00),
      CabinPrice("CA", "S1", 225.00),
      CabinPrice("CA", "S2", 260.00),
      CabinPrice("CB", "M1", 230.00),
      CabinPrice("CB", "M2", 260.00),
      CabinPrice("CB", "S1", 245.00),
      CabinPrice("CB", "S2", 270.00),
    )
    allCabinPrices
}

case class Rate(rateCode: String, rateGroup: String)
case class CabinPrice(cabinCode: String, rateCode: String, price: BigDecimal)
case class BestGroupPrice(cabinCode: String, rateCode: String, price: BigDecimal, rateGroup: String)

case class Promotion(code: String, notCombinableWith: Seq[String])
case class PromotionCombo(promotionCodes: Seq[String])